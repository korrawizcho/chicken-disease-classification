from src.cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()  
    logger.info(f">>>>>> stage {STAGE_NAME} completed!<<<<< \n\n x================x \n")
except Exception as e:
    logger.error(f"stage {STAGE_NAME} error: {e}")
    raise e