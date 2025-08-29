from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_validation import DataValiadtion

from src.datascience import logger

STAGE = "Data Validation"
class DataValidationPipeline:
    def __init__(self):
        pass
    def initiate_data_validation(self):
        try:
            config=ConfigurationManager()
            data_validation_config=config.get_data_validation_config()
            data_validation=DataValiadtion(config=data_validation_config)
            status=data_validation.validate_all_columns()
            logger.info(f"validation status {status}")
        except Exception as e:
            raise e