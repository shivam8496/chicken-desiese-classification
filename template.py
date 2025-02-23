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
    f"src/{projectName}/intity/__init__.py",
    "requirements.py",
    "setup.py",
    "config/config.yaml",
    "params.yaml",
    "dvc.yaml",
    "research/trails.ipynb"
]

for filePath in list_of_file:
    filePath = Path(filePath)
    folder , file =os.split(filePath)
    
    if not os.path.exists(folder):
        os.mkdir(folder,exist_ok=True)
        print(f"folder {folder} created succfully")
    if (not os.path.exists(filePath)) or (os.path.getsize(filePath)==0):
        with open(filePath,"w") as x: pass
        logging.info(f"folder {folder} and file {file} created succfully")
