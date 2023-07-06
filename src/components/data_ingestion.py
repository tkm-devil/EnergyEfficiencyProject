# In this file we will perform data ingestion from source to destination.
# 1. We will read the data from source
# 2. We will save the data in destination

# import the required libraries
import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from dataclasses import dataclass

# Config class for data ingestion
@dataclass
class DataIngestionConfig:
    data_path = os.path.join('notebooks', 'data', 'ENB2012_data_new.csv')
    raw_data_path = os.path.join('artifacts', 'data', 'raw.csv')

# Data ingestion class
class DataIngestion:

    def __init__(self):
        self.config = DataIngestionConfig()

    def create_directory(self):
        directory = os.path.dirname(self.config.raw_data_path)
        os.makedirs(directory, exist_ok=True)

    def initiate_data_ingestion(self):
        try:
            logging.info("Initiating data ingestion")

            logging.info("Reading data from source")
            df = pd.read_csv(self.config.data_path)
            logging.info("Reading data from source completed")

            self.create_directory()

            logging.info("Saving data in destination")
            df.to_csv(self.config.raw_data_path, index=False)
            logging.info("Saving data in destination completed")

            logging.info("Data ingestion completed")
            return self.config.raw_data_path
        except Exception as e:
            logging.error("Error occurred while performing data ingestion")
            raise CustomException("Error occurred while performing data ingestion", e)
