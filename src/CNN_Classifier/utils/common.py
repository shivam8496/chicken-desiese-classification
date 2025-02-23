import os 
from CNN_Classifier import logger
from ensure import ensure_annotations
from pathlib import Path
from box import ConfigBox 
from box.exceptions import BoxValueError
import yaml 


@ensure_annotations
def read_yaml(path_to_yaml:Path)->ConfigBox:
    try:
        with open(path_to_yaml) as file_obj:
            file_content=yaml.safe_load(file_obj)
            logger.info(f"yaml file:{path_to_yaml} file Content loaded")
        return file_content
    except BoxValueError:
        raise ValueError("Cannot Find the file")
    except Exception as e:
        raise e
