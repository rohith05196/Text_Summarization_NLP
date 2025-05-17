from textsummarizer.logging import logger
from textsummarizer.config.configuration import ConfigurationManager
from textsummarizer.components.stage_02_data_validation import DataValidation

class DataValidationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validation_exist_files()
        

if __name__ == '__main__':

    STAGE_NAME = "Second Stage : Data Validation"

    try:
        
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataValidationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    
    except Exception as e:
        logger.exception(e)
        raise e
