# In this file we will completely automate the training and evaluation of the model.

# import the required libraries
import os
import sys
from src.logger import logging
from src.exception import CustomException

# import the required components
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

if __name__ == "__main__":
    
    data_ingestion = DataIngestion()
    raw_data_path = data_ingestion.initiate_data_ingestion()
    logging.info("Raw data path: %s", raw_data_path)

    data_transformation = DataTransformation()
    transformed_data_path, preprocessor_path = data_transformation.initiate_data_transformation()
    logging.info("Transformed data path: %s", transformed_data_path)
    logging.info("Preprocessor path: %s", preprocessor_path)

    model_trainer = ModelTrainer()
    model_path_1, model_path_2, metrics_path = model_trainer.initiate_model_trainig()
    logging.info("Heating Load Model path: %s", model_path_1)
    logging.info("Cooling Load Model path: %s", model_path_2)
    logging.info("Metrics path: %s", metrics_path)

    logging.info("Training pipeline completed successfully!!")