import os
from textsummarizer.logging import logger
from textsummarizer.entities import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validation_exist_files(self)-> bool:
        """
        Check if all required files exist in the directory.
        """
        logger.info("Checking if all required files exist...")
        files = os.listdir("artifacts/data_ingestion/samsum_dataset")
        status = None
        for file in files:
            if file not in self.config.ALL_REQUIRED_FILES:
                status = False
                logger.info(f"File {file} is missing.")
                with open(self.config.STATUS_FILE, 'w') as file:
                    file.write(f" Validatiion status: {status}")
            else:
                status = True
                logger.info("All required files exist.")
                with open(self.config.STATUS_FILE, 'w') as file:
                    file.write(f" Validatiion status: {status}")    

        return status
            
        