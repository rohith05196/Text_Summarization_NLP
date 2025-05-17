from textsummarizer.logging import logger
from textsummarizer.pipeline.stage_01_data_ingestion_pipeline import DataIngestionPipeline


try:
    ingestion = DataIngestionPipeline()
    ingestion.main()
except Exception as e:
    raise e


logger.info("Starting the application")