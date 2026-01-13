from src.mlProject.entity.config_entity import DataTransformationConfig
from src.mlProject.config.configuration import ConfigurationManager
from src.mlProject.components.data_transformation import DataTransformation
from src.mlProject.logger import logging

STAGE_NAME = "Data Transformation Stage"
class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        logging.info("Data Transformation stage started")
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(config=data_transformation_config)
            data_transformation.train_test_spliting()
            logging.info("Data Transformation stage completed")
        except Exception as e:
            logging.error(f"Error in Data Transformation stage: {e}")
            raise e
        
if __name__ == "__main__":
    try:
        pipeline = DataTransformationTrainingPipeline()
        pipeline.main()
    except Exception as e:
        logging.error(f"Error in Data Transformation Pipeline: {e}")
        raise e 
                