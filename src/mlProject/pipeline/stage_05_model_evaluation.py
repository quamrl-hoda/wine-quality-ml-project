from src.mlProject.logger import logging
from src.mlProject.config.configuration import ConfigurationManager
from src.mlProject.components.model_evaluation import ModelEvaluation

STAGE_NAME = "Model Evaluation Stage" 

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
            model_evaluation_config.log_into_mlflow()
        except Exception as e:
            logging.error(f"Error in stage {STAGE_NAME}: {e}")
            raise e
        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx================x") 

if __name__ == "__main__":
    try:
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
    except Exception as e:
        logging.error(f"Error in stage {STAGE_NAME}: {e}")
        raise e
    logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx================x") 