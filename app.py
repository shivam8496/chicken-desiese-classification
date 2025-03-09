from CNN_Classifier import logger
from CNN_Classifier.pipeline.stage_01_data_ingestion import STAGE_NAME,DataIngestionTrainingPipeline

if __name__=="__main__":
    try:
        print(f"\n\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>stage {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n\n")
        obj1=DataIngestionTrainingPipeline()
        obj1.main()
        print(f"\n\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n\n")
        print(" x========================================================================================x")
    except Exception as e:
        logger.exception(e)
        raise e
