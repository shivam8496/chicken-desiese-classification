from CNN_Classifier.components.data_ingestion import DataIngestion
from CNN_Classifier.config.configurations import ConfigurationsManager
from CNN_Classifier import logger


STAGE_NAME = "Data"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationsManager()
        data_config=config.get_data_ingestion_config()
        ingest_data=DataIngestion(config=data_config)
        ingest_data.download_file()
        ingest_data.extract_file()

