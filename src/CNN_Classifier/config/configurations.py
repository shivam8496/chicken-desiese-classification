from CNN_Classifier.constants import *
from CNN_Classifier.utils.common import read_yaml , create_directories
from CNN_Classifier.entity.config_entity import DataIngestionConfig

class ConfigurationsManager:
    def __init__(self,config_filePath=CONFIG_FILE_PATH,params_filePath=PARAMS_FILE_PATH):
        self.config = read_yaml(config_filePath)
        self.params = read_yaml(params_filePath)
        create_directories([self.config.artifacts_root])
    
    def get_data_ingestion_config(self)->DataIngestionConfig:
        create_directories([self.config.data_ingestion.root_dir])

        return DataIngestionConfig(
            root_dir=self.config.data_ingestion.root_dir,
            source_url=self.config.data_ingestion.source_url,
            local_data_file=self.config.data_ingestion.local_data_file,
            unzip_dir=self.config.data_ingestion.unzip_dir
        )

