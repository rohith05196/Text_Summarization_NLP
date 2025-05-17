from urllib import request
import zipfile
import os
from textsummarizer.logging import logger
from textsummarizer.utils.common_func import get_size
from textsummarizer.entities import DataIngestionConfig
from textsummarizer.utils.common_func import create_directories


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_data(self):
        if not os.path.exists(self.config.local_data_file):
            logger.info(f"Downloading file from: {self.config.source_url}")
            request.urlretrieve(self.config.source_url, self.config.local_data_file)
        else:
            logger.info(f"File already exists at: {self.config.local_data_file}.")
            logger.info(f"File size: {get_size(self.config.local_data_file)} bytes.")

    def extract_zip_file(self):
        
        logger.info(f"Extracting file to: {self.config.unzip_dir}")
        create_directories([self.config.unzip_dir])
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_id:
            zip_id.extractall(self.config.unzip_dir)