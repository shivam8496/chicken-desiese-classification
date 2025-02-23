import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO, format='[%(asctime)s:%(message)s]')


projectName="CNN_Classifier"


list_of_file=[
    ".github/workflows/.gitkeep",
    f"src/{projectName}/__init__.py",
    f"src/{projectName}/components/__init__.py",
    f"src/{projectName}/components/__init__.py",
    f"src/{projectName}/utils/__init__.py",
    f"src/{projectName}/config/__init__.py",
    f"src/{projectName}/config/configurations.py",
    f"src/{projectName}/pipeline/__init__.py",
    f"src/{projectName}/entity/__init__.py",
    "requirements.txt",
    "setup.py",
    "config/config.yaml",
    "params.yaml",
    "dvc.yaml",
    "research/trails.ipynb",
    "templates/index.html",
    "app.py"
]

for filePath in list_of_file:
    filePath = Path(filePath)
    folder , file =os.path.split(filePath)
    if(folder!=""):
        if not os.path.exists(folder):
            os.makedirs(folder,exist_ok=True)
            print(f"folder {folder} created succfully")
    if(file!=""):
        if (not os.path.exists(filePath)) or (os.path.getsize(filePath)==0):
            with open(filePath,"w") as x: pass
            logging.info(f"folder {folder} and file {file} created successfully")
        else: logging.info(f"folder {folder} and file {file} already exists")   