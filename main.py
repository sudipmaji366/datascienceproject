from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationPipeline
from src.datascience.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.datascience.pipeline.model_trainer_pipeline import ModelTrainerPipeline
from src.datascience.pipeline.model_evalution_pipeline import ModelEvaluationTrainingPipeline

STAGE = "Data Ingestion"
try:
    logger.info(f">>>>> stage {STAGE} started <<<<<")
    obj = DataIngestionPipeline()
    obj.initiate_data_ingestion()
    logger.info(f">>>>> stage {STAGE} completed <<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE = "Data Validation"

try:
    logger.info(f">>>>> stage {STAGE} started <<<<<")
    obj = DataValidationPipeline()
    obj.initiate_data_validation()
    logger.info(f">>>>> stage {STAGE} completed <<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE = "Data Transformation"

try:
    logger.info(f">>>>> stage {STAGE} started <<<<<")
    obj = DataTransformationPipeline()
    obj.initiate_data_transformation()
    logger.info(f">>>>> stage {STAGE} completed <<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE = "Model Trainer"

try:
    logger.info(f">>>>> stage {STAGE} started <<<<<")
    obj = ModelTrainerPipeline()
    obj.initiate_model_trainer()
    logger.info(f">>>>> stage {STAGE} completed <<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model evaluation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = ModelEvaluationTrainingPipeline()
   data_ingestion.initiate_model_evaluation()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
