from textsummarizer.logging import logger
from textsummarizer.config.configuration import ConfigurationManager
from textsummarizer.components.stage_03_data_transformation import DataTransformation

class DataTransformationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert_data()
        

if __name__ == '__main__':

    STAGE_NAME = "Third Stage : Data Transformation"

    try:
        
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    
    except Exception as e:
        logger.exception(e)
        raise e
