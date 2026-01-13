
from src.mlProject.config.configuration import ConfigurationManager
from src.mlProject.components.model_trainer import ModelTrainer
from src.mlProject.logger import logging

STAGE_NAME = "Model Trainer Stage"
class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        logging.info("Model Trainer stage started")
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer_config = ModelTrainer(config=model_trainer_config)
            model_trainer_config.train()
        except Exception as e:
            logging.error(f"Error in Model Trainer stage: {e}")
            raise e
                
if __name__ == "__main__":
    try:
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        pipeline = ModelTrainerTrainingPipeline()
        pipeline.main()
    except Exception as e:
        logging.error(f"Error in Model Trainer Pipeline: {e}")
        raise e
    