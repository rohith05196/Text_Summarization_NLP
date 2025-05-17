from textsummarizer.logging import logger
from textsummarizer.pipeline.stage_01_data_ingestion_pipeline import DataIngestionPipeline
from textsummarizer.pipeline.stage_02_data_validation_pipeline import DataValidationPipeline
logger.info("First Stage : Data Ingestion")

try:
    ingestion = DataIngestionPipeline()
    ingestion.main()
except Exception as e:
    raise e


logger.info("Second Stage : Data Validation")

try:
    ingestion = DataValidationPipeline()
    ingestion.main()
except Exception as e:
    raise e



