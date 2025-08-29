from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.model_trainer import ModelTrainer

from src.datascience import logger


STAGE = "Model Trainer"

class ModelTrainerPipeline:
    def __init__(self):
        pass
    def initiate_model_trainer(self):
       config = ConfigurationManager()
       model_trainer_config = config.model_trainer_config()
       model_trainer = ModelTrainer(config=model_trainer_config)
       model_trainer.train()