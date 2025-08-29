from src.datascience.config.configuration import ConfigurationManager
from src.datascience.entitity.config_entity import DataValidationConfig
from src.datascience import logger
import pandas as pd
import os

STAGE_NAME = "Data Validation stage"

class DataValiadtion:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self)-> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)

            all_schemas = list(self.config.all_schemas)

            
            for col in all_cols:
                if col not in all_schemas:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")

            return validation_status
        
        except Exception as e:
            raise e

    