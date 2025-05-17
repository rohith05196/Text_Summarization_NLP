from textsummarizer.logging import logger
from textsummarizer.pipeline.stage_01_data_ingestion_pipeline import DataIngestionPipeline
from textsummarizer.pipeline.stage_02_data_validation_pipeline import DataValidationPipeline
from textsummarizer.pipeline.stage_03_data_transformation_pipeline import DataTransformationPipeline

logger.info("First Stage : Data Ingestion")

try:
    ingestion = DataIngestionPipeline()
    ingestion.main()
except Exception as e:
    raise e


logger.info("Second Stage : Data Validation")

try:
    validation = DataValidationPipeline()
    validation.main()
except Exception as e:
    raise e



try:
    transformation = DataTransformationPipeline()
    transformation.main()
except Exception as e:
    raise e


