import os
from textsummarizer.logging import logger
from pathlib import Path
import yaml
from box import ConfigBox
from ensure import ensure_annotations


@ensure_annotations
def read_yaml(file_path: Path) -> ConfigBox:

    with open(file_path, 'r') as f:
        data = yaml.safe_load(f)
        logger.info(f"Read the yaml file: {file_path}")


@ensure_annotations
def create_directory(filedir: Path) -> None:
    os.makedirs(filedir, exist_ok=True)
    logger.info(f"Created directory: {filedir}")

    