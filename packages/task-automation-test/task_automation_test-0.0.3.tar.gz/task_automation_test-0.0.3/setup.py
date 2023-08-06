import pathlib
from setuptools import setup
HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()
setup(
  name="task_automation_test",
  version="0.0.3",
  description="Package contains functions to perform simple task such as FTP transfer, Import to miscrosoft database etc.",
  long_description=README,
  long_description_content_type="text/markdown",
  author="Yogesh Khuha",
  author_email="yogesh.khuha@gmail.com",
  license="MIT",
  packages=["task_automation_test"],
  zip_safe=False
)