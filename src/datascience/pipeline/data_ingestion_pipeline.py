from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_ingestion import DataIngestion
from src.datascience import logger

STAGE = "Data Ingestion" 

class DataIngestionPipeline:
    def __init__(self):
        pass
    
    def initiate_data_ingestion(self):
        
            
            config=ConfigurationManager()
            data_ingestion_config=config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
if __name__=="__main__":
    try:
        logger.info(f">>>>> stage {STAGE} started <<<<<")
        obj=DataIngestionPipeline()
        obj.initiate_data_ingestion()
        logger.info(f">>>>> stage {STAGE} completed <<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
           