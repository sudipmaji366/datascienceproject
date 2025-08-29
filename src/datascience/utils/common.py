import os
import yaml
from src.datascience import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from typing import Any
from pathlib import Path
from box.exceptions import BoxValueError, BoxKeyError

@ensure_annotations
def read_yaml(path_to_yaml:Path) -> ConfigBox:
    """Reads a yaml file and returns

    Args:
        path_to_yaml (Path): Path like input

    Raises:
        e: Raises an exception if file is not found

    Returns:
        ConfigBox: ConfigBox type object
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError as e:
        raise ValueError("yaml file is empty")
    except BoxKeyError as e:
        raise KeyError("Key not found")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories:list):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
    """
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        logger.info(f"created directory at: {path}")

@ensure_annotations
def save_json(path:Path, data:dict):  

    """save dictionary data to json file

    Args:
        path (Path): path to json file
        data (dict): data to be written
    """
    try:
        with open(path,'w') as json_file:
            json.dump(data,json_file,indent=4)
            logger.info(f"json file saved at: {path}")
    except Exception as e:
        raise e  


@ensure_annotations
def load_json(path:Path) -> ConfigBox:
    """load json file and returns ConfigBox object

    Args:
        path (Path): path to json file

    Raises:
        e: raises exception if any

    Returns:
        ConfigBox: ConfigBox type object
    """
    try:
        with open(path) as json_file:
            content=json.load(json_file)
            logger.info(f"json file: {path} loaded successfully")
            return ConfigBox(content)
    except Exception as e:
        raise e
    
@ensure_annotations
def save_bin(data:Any, path:Path):
    """save any kind of data to file

    Args:
        data (Any): data to be saved
        path (Path): path to the file
    """
    try:
        joblib.dump(data,path)
        logger.info(f"binary file saved at: {path}")
    except Exception as e:
        raise e
    
@ensure_annotations
def load_bin(path:Path) -> Any:
    """load binary file and return the data

    Args:
        path (Path): path to the file

    Raises:
        e: raises exception if any

    Returns:
        Any: data stored in the file
    """
    try:
        data=joblib.load(path)
        logger.info(f"binary file loaded from: {path}")
        return data
    except Exception as e:
        raise e