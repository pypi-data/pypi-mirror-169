# -*- coding: utf-8 -*-
__version__ = "0.0.1"
"""
@author: Yogesh

This module contains functions to perform the small tasks such as 
downloading email attachment, FTP upload and FTP download,
importing or appending the csv or txt file to Microsoft SQL server database etc.

Functions
---------
attachment_verification(file_path, files)
    Compares size of downloaded file with the file attached to the email.
download_attachment(email_sender, email_subject, files, download_location, received_duration=1,email_folder="Inbox")
    Downloads attachments from an email.
csv_to_txt(csvfile,txtfile,delimiter='\t',replace_if_exist=True)
    Converts csv file to txt file using delimiter.
ftp_upload_verify(hostname, username, password, ftp_dir, files, filepath,TLS)
    Verifies the uploaded file size with original file size.
ftp_upload(hostname, username, password, ftp_dir, files, filepath,TLS=False)
    Uploads files to the FTP server and compares the uploaded file size with 
    original file size.
ftp_download_verify(hostname, username, password, ftp_dir, files, filepath,TLS)
    Veryfies the file size of the downloaded file with the original file.
ftp_download(hostname, username, password, ftp_dir, files, filepath,TLS=False)
    Downloads files from FTP server and compares the file size of the 
    downloaded file with the original file.
execute_msql(sql_file, con)
    Executes query from '.sql' file.
append_csv_msql(filepath,con,insert_query,has_header=False)
    Appends the .CSV file to the existing table 
    in Microsoft SQL Server database.
append_txt_msql(filepath, con, insert_query,has_header=False,delimiter='|')
    Appends the .txt file to the existing table 
    in Microsoft SQL Server database.
import_csv_msql(filepath,con,create_query,insert_query,has_header)
    Imports the .CSV file to the Microsoft SQL Server database.
    NOTE: This function will drop the table if already exist and will 
        create a new one. 
import_text_msql(filepath, con, create_query, insert_query, has_header)
    Imports .TXT file to the microsoft SQL server database.
    NOTE: This function will drop the table if already exist and will 
        create a new one. 
msql_results_to_file(sql_file, output_file, con, save_as='CSV', header=False)
    Executes query in .sql file and saves resulting table as 'CSV' or 
    'TXT'('|' delimited) file.
query_results_to_file(query, output_file, con, save_as="CSV", header=False)
    Executes the query and saves the result as 'CSV' or 'TXT'('|' delimited) file.
run_msql(con, query)
    Runs SQL query.
send_email(profilename, recipients, CC, subject, email_body, attachments)
    Sends email to the recipients, can also send attachments with email.
send_reply(email_sender, email_subject, reply_body, received_duration=1,email_folder="Inbox")
    Sends reply(Reply all) to the email.
sftp_file_verify(hostname,port,  username, password,ftp_dir,filepath,file)
    After upload or download transaction, compares size of the file on 
    the sftp server with size of the file on the device/network.    
sftp_upload(hostname,port,  username, password,ftp_dir,filepath,file)
    Uploads file to SFTP server.
sftp_download(hostname,port,  username, password,ftp_dir,filepath,file)
    Downloads file from SFTP server.
"""

# In[18]:
import win32com.client
import os
from datetime import datetime, timedelta
import ftplib
import paramiko
import pyodbc
import pandas as pd
import csv
# In[19]: 
def attachment_verification(file_path, files):
    """This function checks for the file at the given location and prints the message if the file(s) exists or not.
    file_path:str
        Folder location of the file.
    files:List
        List of file names which will be checked at the file_path folder.
    """
    for file_name in files:
        if os.path.exists(file_path+file_name):
            print(file_path+file_name+": download successful.")
        else:
            print(file_path+file_name+": file not found.")
        
# In[20]:
def download_attachment(email_sender, email_subject, files, download_location, received_duration=1,email_folder="Inbox"):
    """This function will download the specified attachment file from the outlook email.

    Parameters
    ----------
    email_sender:str
        Email address of the sender.
        i.e.: "xyz@gmail.com"
    email_subject:str
        Subject line of the email from which file needs to be downloaded.
        i.e.: 'email subject'
    files:list
        Names of the files in the email which will be downloaded.
        i.e.: ["File1.txt","File2.csv","File3.txt"]
    download_location:str
        Location of the folder where file needs to be downloaded.
        i.e.: "C:/User/xyz/download/"
    received_duration:integer
        Number specifying how old is email (in days), 
        i.e. if email was received 1 day ago than received_duration should be 1,
        if email was received before 2 days of running the fuction then its value 2 should be entered.
    email_folder:str
        This is useful when email is set to move to the different folder other than Inbox. 
        'email_folder' takes folder name where the function will look for the email.
        Default value for this parameter is Inbox as most of the emails will go to the inbox by default.
        If the email is in subfolder then value will be email_folder="folder1/folder2"
        In above example email will be inside folder2 which is sub folder of folder 1.
        
    Returns
    -------
    """
    outlook = win32com.client.Dispatch('outlook.application')
    mapi = outlook.GetNamespace("MAPI")
    received_dt = datetime.now() - timedelta(days=received_duration)
    received_dt = received_dt.strftime('%m/%d/%Y %H:%M %p')
    email_folder=email_folder.split('/')
    #inbox = mapi.GetDefaultFolder(6) #Inbox folder
    if "Public" in mapi.Folders.Item(1).Name:
        inbox = mapi.Folders.Item(2).Folders[email_folder[0]] #specify the folder
    else:
        inbox = mapi.Folders.Item(1).Folders[email_folder[0]]
    if len(email_folder)>1:
        for i in range(1,len(email_folder)):
            inbox=inbox.Folders[email_folder[i]]
    messages = inbox.Items 
    #email_sender = ''
    #email_subject = ''
    messages = messages.Restrict("[ReceivedTime] >= '"+received_dt+"'")
    try:
        #print(email_sender, email_subject, file_name, download_location, received_duration)
        for message in list(messages):
            if message.Class == 43:
                if message.SenderEmailType=='EX':
                    if message.Sender.GetExchangeUser() != None:
                        sender = message.Sender.GetExchangeUser().PrimarySmtpAddress
                    else:
                        sender = message.Sender.GetExchangeDistributionList().PrimarySmtpAddress
                else:
                    sender=message.SenderEmailAddress
            #print(message.subject)
            if email_subject in message.subject and sender.lower() == email_sender.lower(): #and message.ReceivedTime.strftime('%Y-%m-%d') == '2022-05-17':
                try:
                    #print('inside if')
                    for attachment in message.Attachments:
                        #print('inside loop')
                        #attachment.SaveASFile(os.path.join(outputDir, attachment.FileName))
                        for file_name in files:
                            if attachment.FileName == file_name:
                                attachment.SaveAsFile(download_location + attachment.FileName)
                            #print(f"attachment {attachment.FileName} from {s} saved"
                except Exception as e:
                    print("Error when saving the attachment:" + str(e))
                    raise e
    except Exception as e:
        print("Error when processing emails messages:" + str(e))
        raise e
    attachment_verification(download_location,files)
    
# In[21]:
def csv_to_txt(csvfile,txtfile,delimiter='\t',replace_if_exist=True):
    """This function converts csv file to delimited txt file using specified delimiter.
    
    Parameters
    ----------------------------------------------------------------------------------
    csvfile:str
        'csvfile' contains path and file name of the csv file.
        i.e. csvfile="C:/Users/xyz/Documents/abc.csv"
    txtfile:str
        'txtfile' contains path and file name of the output txt file.
        i.e. txtfile="C:/Users/xyz/Documents/abc.txt"
    delimiter:str
        Will specify which delimiter to use while converting csv to txt.
        Most common delimeters are '\t' for tab delimited file 
        and '|' for pipe delimited file.
    replace_if_exist:boolean
        In case the text file with the given name already exists 
        and if the value is True then file will be replaced,
        if the value is False then file will be appended with new records
        i.e. replace_if_exist = True
    """
    #if file_ext == '.csv':
    if replace_if_exist and os.path.exists(txtfile):
        os.remove(txtfile)
    with open(csvfile,'r',encoding='utf8') as csv_file:
        csv_reader = csv.reader(csv_file)
        # next(csv_reader)  ## skip one line (the first one)
        for line in csv_reader:
            # print(line)
            with open(txtfile, 'a',newline='',encoding='utf8') as new_txt:    #new file has .txt extn
                txt_writer = csv.writer(new_txt, delimiter = delimiter) #writefile
                txt_writer.writerow(line)   #write the lines to file`
# In[21]:
def ftp_upload_verify(hostname, username, password, ftp_dir, files, filepath,TLS):
    """This function verifies the uploaded file using its name and
    by comparing the size of the original file and uploaded file
    
    Parameters
    -------------------------------------------------------------------------------------
    hostname:str
        Hostname of the FTP server.
    username:str
        Username will be used to create connection to the FTP server.
    password:str
        Password will be used to create connection to the FTP server.
    ftp_dir:str
        Location of the directory in the FTP server where the file will be uploaded.
    filename:str
        Name of the file to upload.
    filepath:str
        Path or folder location in which file exist in the computer.
    TLS:boolean
        TLS will be true if Encription: Uses explicit FTP over TLS.
    """
    if TLS :
        ftp_server = ftplib.FTP_TLS(hostname)
        # login after securing control channel
        ftp_server.login(username, password)           
        # switch to secure data connection.. 
        # IMPORTANT! Otherwise, only the user and password is encrypted and
        # not all the file data.
        ftp_server.prot_p()  
    else:
        # Connect FTP Server
        ftp_server = ftplib.FTP(hostname, username, password)
        # force UTF-8 encoding
        ftp_server.encoding = "utf-8"
    
    #Open Server directory from which you want download or upload the file
    ftp_server.cwd(ftp_dir)
    ftp_server.voidcmd('TYPE I')
    # Enter File Name with Extension
    #filename = "abc.csv"
    for file_name in files:
        if file_name in ftp_server.nlst(file_name):
            print(ftp_dir+"/"+file_name+": File location verified.")
            if ftp_server.size(file_name) == os.path.getsize(filepath+file_name):
                print("File size verified.")
                print("FTP file size : " + str(ftp_server.size(file_name)))
                print("Original file size : "+str(os.path.getsize(filepath+file_name)))
            else:
                print("File size does not Match")
                print("FTP file size : " +str(ftp_server.size(file_name)))
                print("Original file size : " +str(os.path.getsize(filepath+file_name)))
        else:
            print(ftp_dir+"/"+file_name+": File not found!")        
    ftp_server.quit()
# In[22]:
def ftp_upload(hostname, username, password, ftp_dir, files, filepath,TLS=False):
    """This function uploads file to the FTP server in specified directory using the credentials
    
    Parameters
    ------------------------------------------------------------------------
    hostname:str
        Hostname of the FTP server.
    username:str
        Username will be used to create connection to the FTP server.
    password:str
        Password will be used to create connection to the FTP server
    ftp_dir:str
        Location of the directory in the FTP server where the file will be uploaded.
        i.e. '/folder1/insidefolder/'
    filename:str
        Name of the file to upload.
        i.e.: ["File1.txt","File2.csv","File3.txt"]
    filepath:str
        Path or folder location in which file exist in the computer.
    TLS:boolean
        TLS will be true if Encription: Uses explicit FTP over TLS.
    """
    # Connect FTP Server
    if TLS :
        ftp_server = ftplib.FTP_TLS(hostname)
        # login after securing control channel
        ftp_server.login(username, password)           
        # switch to secure data connection.. 
        # IMPORTANT! Otherwise, only the user and password is encrypted and
        # not all the file data.
        ftp_server.prot_p()  
    else:
        # Connect FTP Server
        ftp_server = ftplib.FTP(hostname, username, password)
        # force UTF-8 encoding
        ftp_server.encoding = "utf-8"
    
    #Open Server directory from which you want download or upload the file
    ftp_server.cwd(ftp_dir)
    print("Connection successful.")
    print("Uploading files now.")
    # Enter File Name with Extension
    #filename = "abc.csv"
    for file_name in files:
        #print(file_name)
        with open(filepath+file_name, "rb") as file:
            # Command for Uploading the file "STOR filename"
            ftp_server.storbinary(f"STOR {file_name}", file)
        #print(ftp_server.size(file_name))
    ftp_server.quit()
    ftp_upload_verify(hostname, username, password, ftp_dir, files, filepath,TLS)
# In[23]:
def ftp_download_verify(hostname, username, password, ftp_dir, files, filepath,TLS):
    """This function verifies the downloaded file using its name and
    by comparing the size of the original file and downloaded file
    
    Parameters
    -------------------------------------------------------------------------------------
    hostname:str
        Hostname of the FTP server.
    username:str
        Username will be used to create connection to the FTP server.
    password:str
        Password will be used to create connection to the FTP server
    ftp_dir:str
        Location of the directory in the FTP server where the file will be uploaded.
    filename:str
        Name of the file to upload.
    filepath:str
        Path or folder location in which file exist in the computer.
    TLS:boolean
        TLS will be true if Encription: Uses explicit FTP over TLS.
    """
    if TLS :
        ftp_server = ftplib.FTP_TLS(hostname)
        # login after securing control channel
        ftp_server.login(username, password)           
        # switch to secure data connection.. 
        # IMPORTANT! Otherwise, only the user and password is encrypted and
        # not all the file data.
        ftp_server.prot_p()  
    else:
        # Connect FTP Server
        ftp_server = ftplib.FTP(hostname, username, password)
        # force UTF-8 encoding
        ftp_server.encoding = "utf-8"
    ftp_server.cwd(ftp_dir)
    # Enter File Name with Extension
    #filename = "abc.csv"
    ftp_server.voidcmd('TYPE I') #set the server to binary which will not give error while getting the size
    for file_name in files:
        if os.path.exists(filepath+file_name):
            print(filepath+file_name+": download location verified.")
            if ftp_server.size(file_name) == os.path.getsize(filepath+file_name):
                print("File size verified.")
                print("FTP file size : " + str(ftp_server.size(file_name)))
                print("Downloaded file size : " + str(os.path.getsize(filepath+file_name)))
            else:
                print("File size does not Match")
                print("FTP file size : " + str(ftp_server.size(file_name)))
                print("Downloaded file size : " + str(os.path.getsize(filepath+file_name)))
        else:
            print(filepath+file_name+": file not found.")
    ftp_server.quit()
# In[24]:
def ftp_download(hostname, username, password, ftp_dir, files, filepath,TLS=False):
    """This function uploads file to the FTP server in specified directory using the credentials
    
    Parameters
    -----------------------------------------------------------------------
    hostname:str
        Hostname of the FTP server.
    username:str
        Username will be used to create connection to the FTP server.
    password:str
        Password will be used to create connection to the FTP server
    ftp_dir:str
        Location of the directory in the FTP server from where the file will be downloaded.
        i.e. '/folder1/insidefolder/'
    files:list
        List of the file names to download.
        i.e.: ["File1.txt","File2.csv","File3.txt"]
    filepath:str
        Path or folder location where file will be downloaded.
        i.e. filepath = "C:/Users/XYZ/Download/"
    TLS:boolean
        TLS will be true if Encription: Uses explicit FTP over TLS.
    """
    if TLS :
        ftp_server = ftplib.FTP_TLS(hostname)
        # login after securing control channel
        ftp_server.login(username, password)           
        # switch to secure data connection.. 
        # IMPORTANT! Otherwise, only the user and password is encrypted and
        # not all the file data.
        ftp_server.prot_p()  
    else:
        # Connect FTP Server
        ftp_server = ftplib.FTP(hostname, username, password)
        # force UTF-8 encoding
        ftp_server.encoding = "utf-8"
    
    #Open Server directory from which you want download or upload the file
    ftp_server.cwd(ftp_dir)
    print("Connection successful.")
    print("Downloading files now.")
    for file_name in files:    
        with open(filepath+file_name, "wb") as file:
            # Command for Downloading the file "RETR filename"
            ftp_server.retrbinary(f"RETR {file_name}", file.write)
        # Get list of files
        #ftp_server.dir()
        # Display the content of downloaded file
        #file= open(filename, "r")
        #print('File Content:', file.read())
        # Close the Connection
    ftp_server.quit()
    ftp_download_verify(hostname, username, password, ftp_dir, files, filepath,TLS)
# In[ ]:
def execute_msql(sql_file, con):
    """
    This function executes query in sql file 
    
    
    Parameters
    -----------------------------------------------------------------------
    sql_file:str
        Address or path to sql file which contains the query.
        i.e. sql_file="C:/Users/xyz/Downloads/test.sql"
    con:Object
        connection object is used to create connection with the database.
        i.e. con = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                              "Server=ABCD12-EF3GHI45.xyz.net;"
                              "Database=database_name;"
                              "Trusted_Connection=yes;")
    """
    try:
        cursor=con.cursor()
        query = ""
        with open(sql_file) as infile:
            for line in infile:
                query = query+line+" "
            print("Processing...\n"+query)
            cursor.execute(query)
            #for row in cursor:
                #print('row = %r' % (row,))
        con.commit()
        con.close()
        print("Query completed.")
    except Exception as e:
        con.close()
        raise e
# In[]:
def append_csv_msql(filepath,con,insert_query,has_header=False):
    """This function import(append) the csv file into the existing table 
    in Microsoft SQL Server database.
    
    Parameters
    -----------------------------------------------------------------------
    filepath:str
        Address or path from where csv file will be imported.
        i.e. filepath="C:/Users/xyz/Downloads/abc.csv"
    con:Object
        connection object is used to create connection with the database.
        i.e. con = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                              "Server=ABCD12-EF3GHI45.xyz.net;"
                              "Database=database_name;"
                              "Trusted_Connection=yes;")
    insert_query:str
        Query to insert the values into the table.
        i.e.insert_query = '''
                    INSERT INTO test_table (num, day)
                    VALUES (?,?)
    has_header:boolean
        If CSV file has header then has_header=True, if CSV has no header then has_header=False
    """
    
    data = pd.read_csv(filepath, header= 0 if has_header else None, dtype=object)
    data = data.fillna('')
    #df = pd.DataFrame(data)
    print("Appending data to the table from :"+filepath)
    try:
        cursor = con.cursor()
        cursor.fast_executemany = True
        print("Importing data from "+filepath+"\n")
        #for d in data.values.tolist():
        #    print(d)
        #    cursor.execute(insert_query,d)
        cursor.executemany(insert_query, data.values.tolist())
        con.commit()
        con.close()
        print("Data imported successfully.")
    except Exception as e:
        con.close()
        raise e    
# In[ ]:
def append_txt_msql(filepath, con, insert_query,has_header=False,delimiter='|'):
    """

    This function import(append) the txt file 
    into the existing table in Microsoft SQL Server database. 
    
    
    Parameters
    -----------------------------------------------------------------------
    filepath:str
        Address or path from where txt file will be imported.
        i.e. filepath="C:/Users/xyz/Downloads/abc.txt"
    con:Object
        connection object is used to create connection with the database.
        i.e. con = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                              "Server=ABCD12-EF3GHI45.xyz.net;"
                              "Database=database_name;"
                              "Trusted_Connection=yes;")
    insert_query:str
        Query to insert the values into the table.
        i.e.   insert_query = '''
                      INSERT INTO test_table (num, day)
                      VALUES (?,?)
                      '''
    has_header:boolean
        If text file has header then set has_header=True, if text file has no header then set has_header=False
    delimiter:str
        Delimiter for the text file, by default txt file will be considered '|'(pipe) delimited if not specified.
        i.e. delimiter='|' or delimeter='\t'(for tab delimited file)
    """
    try:
        cursor=con.cursor()
        cursor.fast_executemany = True
        #data = pd.read_table(filepath,delimiter="|",header= 0 if has_header else None)
        data = pd.read_csv(filepath,delimiter=delimiter,header= 0 if has_header else None, dtype=object)
        data = data.fillna('')
        print("Importing data from "+filepath+"\n")
        #print(data)
        cursor.executemany(insert_query, data.values.tolist())
        con.commit()
        con.close()
        print("Data imported successfully.")
    except Exception as e:
        con.close()
        raise e
# In[ ]:
def import_csv_msql(filepath,con,create_query,insert_query,has_header):
    """This function drops the table if it exists and import the csv file and 
    creates new table in Microsoft SQL Server database.
        
    Parameters
    -----------------------------------------------------------------------
    filepath:str
        Address or path from where csv file will be imported.
        i.e. filepath="C:/Users/xyz/Downloads/abc.csv"
    con:Object
        connection object is used to create connection with the database.
        i.e. con = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                              "Server=ABCD12-EF3GHI45.xyz.net;"
                              "Database=database_name;"
                              "Trusted_Connection=yes;")
    create_query:str
        Query to create a new table.
        i.e. create_query = '''IF OBJECT_ID('dbo.test_table') IS NOT NULL
            DROP TABLE dbo.test_table
            CREATE TABLE test_table (
        			num int,
        			day nvarchar(50)
        			)
                       '''    
    insert_query:str
        Query to insert the values into the table.
        i.e.insert_query = '''
                    INSERT INTO test_table (num, day)
                    VALUES (?,?)
                    '''
    has_header:boolean
        If CSV file has header then has_header=True, if CSV has no header then has_header=False
    """
    #data = pd.read_csv(filepath,header= 0 if has_header else None,dtype=object)
    #df = pd.DataFrame(data)
    data = pd.read_csv(filepath,header= 0 if has_header else None, dtype = str)
    data = data.fillna('')
    #print(df)   
    try:
        cursor = con.cursor()
        cursor.fast_executemany = True
        print("Importing data from "+filepath)
        cursor.execute(create_query)
        #for d in data.values.tolist():
        #    print(d)
        #    cursor.execute(insert_query,d)
        cursor.executemany(insert_query, data.values.tolist())
        con.commit()
        con.close()
        print("Data imported successfully.")
    except Exception as e:
        con.close()
        raise e
# In[ ]:
def import_text_msql(filepath, con, create_query, insert_query, has_header,delimiter='|'):
    """This function drops the table if it exists import the txt file and 
    creates new table in Microsoft SQL Server database.
    
    Parameters
    -----------------------------------------------------------------------
    filepath:str
        Address or path from where txt file will be imported.
        i.e. filepath="C:/Users/xyz/Downloads/abc.txt"
    con:Object
        connection object is used to create connection with the database.
        i.e. con = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                              "Server=ABCD12-EF3GHI45.xyz.net;"
                              "Database=database_name;"
                              "Trusted_Connection=yes;")
    create_query:str
        Query to create a new table.
        i.e. create_query = '''IF OBJECT_ID('dbo.test_table') IS NOT NULL
            DROP TABLE dbo.test_table
            CREATE TABLE test_table (
        			num int,
        			day nvarchar(50)
        			)
                       '''  
    insert_query:str
        Query to insert the values into the table.
        i.e.insert_query = '''
                    INSERT INTO test_table (num, day)
                    VALUES (?,?)
                    '''
    has_header:boolean
        If text file has header then set has_header=True, if text file has no header then set has_header=False
    delimiter:str
        Delimiter for the text file, by default txt file will be considered '|'(pipe) delimited if not specified.
        i.e. delimiter='|' or delimeter='\t'(for tab delimited file)
    """
    try:
        cursor=con.cursor()
        cursor.execute(create_query)
        print("Table created.")
        cursor.fast_executemany = True
        data = pd.read_csv(filepath,delimiter=delimiter,header= 0 if has_header else None, dtype = str)
        data = data.fillna('')
        print("Importing data from "+filepath+"\n")
        #try:
        cursor.executemany(insert_query, data.values.tolist())
        #for d in data.values.tolist():
        #    print(d)
        #    cursor.execute(insert_query,d)
        con.commit()
        con.close()
        print("Data imported successfully.")
        #except Exception as e:
        #    con.close()
        #    print("error"+str(e))
    except Exception as e:
        con.close()
        raise e

# In[ ]:
def msql_results_to_file(sql_file, output_file, con, save_as='CSV', header=False):
    """
    This function executes query in sql file and saves the results as-
    csv or pipe('|') delimited txt file.
    
    
    Parameters
    -----------------------------------------------------------------------
    sql_file:str
        Address or path to sql file which contains the query.
        i.e. sql_file="C:/Users/xyz/Downloads/test.sql"
    con:Object
        connection object is used to create connection with the database.
        i.e. con = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                              "Server=ABCD12-EF3GHI45.xyz.net;"
                              "Database=database_name;"
                              "Trusted_Connection=yes;")
    output_file:str
        Path and name of the output csv file which will store the result of the
        executed query in sql_file.
        i.e. output_file="C:/Users/xyz/Downloads/sample.csv"
    save_as:str
        save_as can have two values CSV or TXT, which will save the results-
        in specified format.
    header:boolean
        'header' is boolean flag if true, output file will have header row,
        if false then output file will not have headers.
    """
    try:
        cursor=con.cursor()
        query = ""
        with open(sql_file) as infile:
            #header = infile.readline()
            for line in infile:
                #print(line)
                query = query+line+" "
            print("Processing...\n"+query)
            cursor.execute(query)
            #for row in cursor:
                #print('row = %r' % (row,))
            if save_as.lower()=='csv':
                with open(output_file,'w') as txtfile:
                    if header == True:
                        txtfile.write(','.join([str(x[0]) for x in cursor.description]))
                        txtfile.write('\n')
                    for row in cursor:
                        txtfile.write(','.join([('NULL' if str(row[i])=='None' else str(row[i]).strip()) for i in range(0,row.__len__())] ))
                        txtfile.write('\n')
                    #txtfile.write('\n')
            elif save_as.lower()=='txt':
                with open(output_file,'w') as txtfile:
                    if header == True:
                        txtfile.write('|'.join([str(x[0]) for x in cursor.description]))
                        txtfile.write('\n')
                    for row in cursor:
                        txtfile.write('|'.join([('NULL' if str(row[i])=='None' else str(row[i])) for i in range(0,row.__len__())] ))
                        txtfile.write('\n')
                    #txtfile.write('\n')
        con.commit()
        con.close()
        print("Result file created successfully.")
    except Exception as e:
        con.close()
        raise e
# In[ ]:
def query_results_to_file(query, output_file, con, save_as="CSV", header=False):
    """
    This function takes query as argument then executes query 
    and saves the results as csv file.
    
    Parameters
    -----------------------------------------------------------------------
    query:str
        Query that needs to be executed.
        i.e. query = '''
                    select * from test_table
                        '''    
    con:Object
        Connection object is used to create connection with the database.
        i.e. con = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                              "Server=ABCD12-EF3GHI45.xyz.net;"
                              "Database=database_name;"
                              "Trusted_Connection=yes;")
    output_file:str
        Path and name of the output csv file which will store the result of the
        executed query in sql_file.
        i.e. output_file="C:/Users/xyz/Downloads/sample.csv"
    save_as:str
        save_as can have two values CSV or TXT, which will save the results-
        in specified format.
    header:boolean
        'header' is boolean flag if true, output file will have header row,
        if false then output file will not have headers.
    """
    try:
        cursor = con.cursor()
        cursor.execute(query)  
        print("Processing...\n"+query)
        if save_as.lower()=='csv':
            with open(output_file, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                if header == True:
                    writer.writerow([x[0] for x in cursor.description])  # column headers
                for row in cursor:
                    #print(row)
                    writer.writerow(row)
        elif save_as.lower()=='txt':
            with open(output_file,'w') as txtfile:
                if header == True:
                    txtfile.write('|'.expandtabs(8).join([x[0] for x in cursor.description]))
                    txtfile.write('\n')
                for row in cursor:
                    #print(row)
                    txtfile.write('|'.expandtabs(8).join([row[i] for i in range(0,row.__len__())] ))
        con.commit()
        con.close()
        print("File created successfully.")
    except Exception as e:
        con.close()
        raise e
# In[ ]:
def run_msql(con, query):
    """
    This function executes query.
    
    Parameters
    -----------------------------------------------------------------------
    query:str
        Query that needs to be executed.
        i.e. query = '''
                    select * from test_table
                        '''    
    con:Object
        connection object is used to create connection with the database.
        i.e. con = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                              "Server=ABCD12-EF3GHI45.xyz.net;"
                              "Database=database_name;"
                              "Trusted_Connection=yes;")
    """
    try:
        cursor = con.cursor()
        print('Executing query...')
        cursor.execute(query)    
        #print([x[0] for x in cursor.description])
        #for row in cursor:
        #    print('row = %r' % (row,))
        con.commit()
        con.close()
        print('Query executed successfully')
    except Exception as e:
        con.close()
        raise e
# In[ ]:
def send_email(profilename, recipients, CC, subject, email_body, attachments=[]): 
    """
    This function sends email with or without attachments.
    
    Parameters
    -----------------------------------------------------------------------
    profilename:str
        profilename is your(sender's) email address.
        i.e. profilename= "xyz@gmail.com"
    recipients:str
        Enter the recipients, if multiple recipients 
        then separate the email addresses with ';'.
        i.e. recipients= "xyz@gmail.com; abc@gmail.com"
    CC:str
        Enter email address to CC, similar to recipients multiple email addresses
        needs to separated by ';'. 
        i.e. CC= "xyz@gmail.com; abc@gmail.com"
        if there is no need for CC then keep CC="".
    subject:str
        Enter email subject.
        i.e. subject="Test subject"
    email_body:str
        Enter email body
        i.e. email_body=  '''test body'''
    attachments:list
        attachments is list of strings, which contains filepath to the file
        that needs to be attached.
        i.e. attachments = ["C:/Users/xyz/Downloads/sample.txt","C:/Users/xyz/Downloads/abc.csv"]
        if there is no attachment to send then keep attachments = []
    """
    #s = win32com.client.Dispatch("Mapi.Session")
    o = win32com.client.Dispatch("Outlook.Application")
    #mapi = o.GetNameSpace("MAPI")
    #s.Logon(profilename)
    Msg = o.CreateItem(0)
    Msg.To = recipients
    if CC != "":
        Msg.CC = CC
    #Msg.BCC = "address"
    Msg.Subject = subject
    Msg.Body = email_body
    for attachment in attachments:
        Msg.Attachments.Add(attachment)
    #attachment1 = "Path to attachment no. 1"
    #attachment2 = "Path to attachment no. 2"
    #Msg.Attachments.Add(attachment1)
    #Msg.Attachments.Add(attachment2)
    Msg.Send()
# In[ ]:
def send_reply(email_sender, email_subject, reply_body, received_duration=1,email_folder="Inbox"):
    """This function will send the reply to the specified email in the outlook.

    Parameters
    ----------
    email_sender:str
        Email address of the sender.
        i.e.: email_sender = "xyz@gmail.com"
    email_subject:str
        Subject line of the email to which reply needs to be sent.
        i.e. subject="Test subject"
    reply_body:str
        'reply_body' contains the message to send as reply.
        i.e. reply_body = 'This is reply body in single line.\nThanks.'
        i.e. reply_body = '''This is message body-
         with multiple lines
         Thanks.'''
    received_duration:integer
        Number specifying how old is email in days, 
        i.e. if email was received 1 day ago than received_duration should be 1,
        if email was received within 2 days of running the fuction then it value 2 should be entered.
    email_folder:str
        This is useful when email is set to move to the different folder other than Inbox. 
        'email_folder' takes folder name where the function will look for the email.
        Default value for this parameter is Inbox as most of the emails will go to the inbox by default.
        If the email is in subfolder then value will be email_folder="folder1/folder2"
        In above example email will be inside folder2 which is sub folder of folder 1.

    Returns
    -------
    """
    outlook = win32com.client.Dispatch('outlook.application')
    mapi = outlook.GetNamespace("MAPI")
    received_dt = datetime.now() - timedelta(days=received_duration)
    received_dt = received_dt.strftime('%m/%d/%Y %H:%M %p')
    email_folder=email_folder.split('/')
    #inbox = mapi.GetDefaultFolder(6) #Inbox folder
    if "Public" in mapi.Folders.Item(1).Name:
        inbox = mapi.Folders.Item(2).Folders[email_folder[0]] #specify the folder
    else:
        inbox = mapi.Folders.Item(1).Folders[email_folder[0]]
    if len(email_folder)>1:
        for i in range(1,len(email_folder)):
            inbox=inbox.Folders[email_folder[i]]
    messages = inbox.Items 
    #email_sender = 'xyz@gmail.com'
    #email_subject = 'email test'
    messages = messages.Restrict("[ReceivedTime] >= '"+received_dt+"'")
    try:
        #print(email_sender, email_subject, file_name, download_location, received_duration)
        for message in list(messages):
            if message.Class == 43:
                if message.SenderEmailType=='EX':
                    if message.Sender.GetExchangeUser() != None:
                        sender = message.Sender.GetExchangeUser().PrimarySmtpAddress
                    else:
                        sender = message.Sender.GetExchangeDistributionList().PrimarySmtpAddress
                else:
                    sender=message.SenderEmailAddress
            #print(message.subject)
            if email_subject in message.subject and sender.lower() == email_sender.lower(): #and message.ReceivedTime.strftime('%Y-%m-%d') == '2022-05-17':
                try:
                    reply = message.ReplyAll()
                    reply.Body = reply_body+reply.Body
                    reply.Send()
                    break
                except Exception as e:
                    print("Error when sending reply:" + str(e))
                    raise e
    except Exception as e:
        print("Error when processing emails messages:" + str(e))
        raise e
# In[ ]:
def sftp_file_verify(hostname,port,  username, password,ftp_dir,filepath,file):
        """This function compares the size of the same file on the sftp server and oon device.
        
        Parameters
        ------------------------------------------------------------------------
        hostname:str
            Hostname of the SFTP server.
        port:int
            Port number will be used to create connection to the SFTP server.
        username:str
            Username will be used to create connection to the SFTP server.
        password:str
            Password will be used to create connection to the SFTP server
        ftp_dir:str
            Location of the directory in the SFTP server from where the file will be downloaded.
            i.e. '/folder1/insidefolder'
        filepath:str
            Path or folder location in which file exist in the computer.
            i.e. filepath = "C:/Users/XYZ/Download/"
        file:str
            file is the name of the file to download.
            i.e.: "File1.txt"
        """    
        ssh_client=paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname,port,username,password)
        ftp = ssh_client.open_sftp()
        ftp.chdir('.')
        ftp.chdir(ftp_dir)
        if file in ftp.listdir():
            ftp_dir = ftp_dir+file
            stat = ftp.stat(ftp_dir)
            if stat.st_size == os.path.getsize(filepath+file):
                print("File size verified.")
                print("FTP file size : " + str(stat.st_size))
                print("Device file size : "+str(os.path.getsize(filepath+file)))
            else:
                print("File size does not match.")
                print("FTP file size : " + str(stat.st_size))
                print("Device file size : "+str(os.path.getsize(filepath+file)))
            #lstatout=str(ftp.lstat(i)).split()[0]
            #if 'd' not in lstatout: 
            #    print (i)
        else:
            print(ftp_dir+"/"+file+": File not found!")
        '''try:
           stat = ftp.stat(ftp_dir)
           print(stat.st_size)
        except IOError:
           print('copying file')
           # ftp.put('deleteme.txt', '/tmp/deleteme.txt')'''
        ssh_client.close()
# In[ ]:
def sftp_upload(hostname,port,  username, password,ftp_dir,filepath,file):
    """This function uploads file to the SFTP server in specified directory using the credentials
    
    Parameters
    ------------------------------------------------------------------------
    hostname:str
        Hostname of the SFTP server.
    port:int
        Port number will be used to create connection to the SFTP server.
    username:str
        Username will be used to create connection to the SFTP server.
    password:str
        Password will be used to create connection to the SFTP server
    ftp_dir:str
        Location of the directory in the SFTP server where the file will be uploaded.
        i.e. '/folder1/insidefolder/'
    filepath:str
        Path or folder location in which file exist in the computer.
        i.e. filepath = "C:/Users/XYZ/Download/"
    file:str
        file is the name of the file to upload.
        i.e.: "File1.txt"
    """
    ssh_client=paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname,port,username,password)
    ftp = ssh_client.open_sftp()
    ftp.chdir('.')
    ftp.chdir(ftp_dir)
    ftp_dir2=ftp_dir+file
    filepath2=filepath+file
    #print(ftp_dir)
    ftp.put(filepath2, ftp_dir2)
    #print(ftp.getcwd())
    sftp_file_verify(hostname, port, username, password, ftp_dir, filepath, file)
# In[ ]:
def sftp_download(hostname,port,  username, password,ftp_dir,filepath,file):
    """This function downloads file to the SFTP server in specified directory using the credentials
    
    Parameters
    ------------------------------------------------------------------------
    hostname:str
        Hostname of the SFTP server.
    port:int
        Port number will be used to create connection to the SFTP server.
    username:str
        Username will be used to create connection to the SFTP server.
    password:str
        Password will be used to create connection to the SFTP server
    ftp_dir:str
        Location of the directory in the SFTP server from where the file will be downloaded.
        i.e. '/folder1/insidefolder/'
    filepath:str
        Path or folder location in which file exist in the computer.
        i.e. filepath = "C:/Users/XYZ/Download/"
    file:str
        file is the name of the file to download.
        i.e.: "File1.txt"
    """
    
    ssh_client=paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname,port,username,password)
    ftp = ssh_client.open_sftp()
    ftp.chdir('.')
    ftp_dir= ftp_dir+file
    filepath=filepath+file
    #ftp.chdir(ftp_dir)
    ftp.get(ftp_dir, filepath)
    #print(ftp.getcwd())
    sftp_file_verify(hostname, port, username, password, ftp_dir, filepath, file)







