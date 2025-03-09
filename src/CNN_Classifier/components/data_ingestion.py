from CNN_Classifier.entity.config_entity import DataIngestionConfig
from CNN_Classifier import logger
import urllib.request as request
import zipfile
import os 

class DataIngestion:
    def __init__(self,config=DataIngestionConfig):
        self.config=config

    def download_file(self):
        # if not os.path.exists(self.config.local_data_file):
        filename , header = request.urlretrieve(
            url=self.config.source_url,
            filename=self.config.local_data_file)
        logger.info(f"file {filename} created succesfully with info :{header}")
        # else:
        #     logger.info(f"file {self.config.local_data_file} has already been created ")

    def extract_file(self):
        
        print("Extracting File ..........")
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, "r") as zipfile_ref:
            zipfile_ref.extractall(unzip_path)
        logger.info(f"file {self.config.local_data_file} Extracted Successfully at {unzip_path} ")
        


if __name__=="__main__":
    from CNN_Classifier.config.configurations import ConfigurationsManager 
    try:
        config = ConfigurationsManager()
        ingest_data_config = config.get_data_ingestion_config()
        ingest_data = DataIngestion(config=ingest_data_config)
        ingest_data.download_file()
        ingest_data.extract_file()

    except Exception as e:
        raise e



