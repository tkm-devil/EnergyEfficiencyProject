# In this file we will perform data transformation on the data
# We will perform the following steps:
# 1. Load the saved data from previous step
# 2. Perform data transformation
# 3. Save the transformed data

# import the required libraries
import os
import sys
from src.logger import logging
from src.exception import CustomException
from src.utils import save_object
import pandas as pd
from dataclasses import dataclass

# sklearn libraries
from sklearn.preprocessing import RobustScaler # found to be the best scaler for this dataset
from sklearn.pipeline import Pipeline # to create a pipeline of transformations
from sklearn.compose import ColumnTransformer # to create a pipeline of transformations
from sklearn.impute import SimpleImputer # to impute missing values

# Config class for data transformation
@dataclass
class DataTransformationConfig:
    raw_data_path = os.path.join('artifacts', 'data', 'raw.csv')
    transformed_data_path = os.path.join('artifacts', 'data', 'transformed.csv')
    preprocessor_path = os.path.join('artifacts', 'models', 'preprocessor.pkl')

# Data transformation class
class DataTransformation:

    def __init__(self):
        self.config = DataTransformationConfig()

    def create_directories(self):
        for path in [self.config.transformed_data_path, self.config.preprocessor_path]:
            directory = os.path.dirname(path)
            os.makedirs(directory, exist_ok=True)

    def create_preprocessor(self):
        try:
            logging.info("Creating preprocessor")

            # define columns to be preprocessed
            columns = ['Relative_Compactness', 'Surface_Area', 'Wall_Area', 'Roof_Area', 
                        'Overall_Height', 'Orientation', 'Glazing_Area', 'Glazing_Area_Distribution']
            
            # define the pipeline
            logging.info("Creating pipeline")
            pipeline = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='median')),
                ('scaler', RobustScaler())
            ])
            logging.info("Pipeline created successfully")

            # define the preprocessor
            preprocessor = ColumnTransformer(transformers=[
                ('preprocessor', pipeline, columns)
            ])
            
            logging.info("Preprocessor created successfully")
            return preprocessor
        except Exception as e:
            logging.error("Error occurred while creating preprocessor")
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self):
        try:
            logging.info("Initiating data transformation")

            # load the raw data
            logging.info("Loading raw data")
            raw_data = pd.read_csv(self.config.raw_data_path)
            logging.info("Raw data loaded successfully")

            # create the preprocessor
            logging.info("Loading preprocessor")
            preprocessor = self.create_preprocessor()
            logging.info("Preprocessor loaded successfully")

            # List of columns to be transformed
            columns = ['Relative_Compactness', 'Surface_Area', 'Wall_Area', 'Roof_Area', 
                        'Overall_Height', 'Orientation', 'Glazing_Area', 'Glazing_Area_Distribution']

            # fit transform the data
            transformed_data = preprocessor.fit_transform(raw_data[columns])

            # add the target columns
            transformed_df = pd.DataFrame(transformed_data, columns=columns)

            # Add the 'Heating_Load' and 'Cooling_Load' columns to the transformed data
            transformed_df['Heating_Load'] = raw_data['Heating_Load']
            transformed_df['Cooling_Load'] = raw_data['Cooling_Load']

            # create the directories
            self.create_directories()

            # save the preprocessor
            save_object(preprocessor, self.config.preprocessor_path)

            # save the transformed data
            transformed_df.to_csv(self.config.transformed_data_path, index=False)

            logging.info("Data transformation completed successfully")
            return (
                self.config.transformed_data_path, 
                self.config.preprocessor_path
                )
        except Exception as e:
            logging.error("Error occurred while performing data transformation")
            raise CustomException(e,sys)

