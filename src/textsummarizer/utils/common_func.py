import os
from box.exceptions import BoxValueError
import yaml
from textsummarizer.logging import logger
import json
from typeguard import typechecked
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


@typechecked
def read_yaml(path_to_yaml: Path) -> ConfigBox:

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"Yaml file: {path_to_yaml} has been loaded succesfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

@typechecked
def save_json(path: Path, data: dict):

    with open(path, 'w') as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at the location: {path}")
 

@typechecked
def load_json(path: Path) -> ConfigBox:
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file: {path} loaded succesfully")

    return ConfigBox(content)

@typechecked
def get_size(path: Path) -> str:
    size_in_kb = round(os.path.getsize(path)/1024)
    return f" {size_in_kb} KB"


@typechecked
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")