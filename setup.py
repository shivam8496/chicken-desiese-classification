import setuptools
from  os import system
with open("README.md","r", encoding="utf-8") as f:
    desc=f.read()

__version__="0.0.0.0"

author_name="shivam8496"
repo_name="chicken-desiese-classification"
project_name="CNN_Classifier"

setuptools.setup(
    name= project_name,
    version =__version__,
    long_description = desc,
    author=author_name,
    author_email= "shivamsingh8496@gmail.com",
    url= f"https://github.com/{author_name}/{repo_name}",
    project_urls={
    "Bug Tracker":f"https://github.com/{author_name}/{repo_name}/issues"
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)

