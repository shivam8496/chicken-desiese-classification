import os 
from CNN_Classifier import logger
from ensure import ensure_annotations
from pathlib import Path
from box import ConfigBox 
from box.exceptions import BoxValueError
import yaml 



@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e




@ensure_annotations
def create_directories(path_to_dir:list,verbose=True):
    for path in path_to_dir:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"created the file at: {path}")



@ensure_annotations
def get_size(path:Path) -> str:
    
    size=round(os.path.getsize(path)/1024)

    return f"~ size {size}KB"
    