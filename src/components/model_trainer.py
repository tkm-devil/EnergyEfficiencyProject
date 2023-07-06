# In this file we will train and evaluate the model

# import the required libraries
import os
import sys
from src.logger import logging
from src.exception import CustomException
from src.utils import save_object
import pandas as pd
from dataclasses import dataclass

# model
# from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor

# sklearn libraries
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Config class for model trainer
@dataclass
class ModelTrainerConfig:
    transformed_data_path: str = os.path.join('artifacts', 'data', 'transformed.csv')
    model_path_1: str = os.path.join('artifacts', 'models', 'heating_load_model.pkl')
    model_path_2: str = os.path.join('artifacts', 'models', 'cooling_load_model.pkl')
    metrics_path: str = os.path.join('artifacts', 'metrics', 'metrics.json')  

# Model trainer class
class ModelTrainer:

    def __init__(self):
        self.config = ModelTrainerConfig()

    def create_directories(self):
        for path in [self.config.model_path_1, self.config.model_path_2, self.config.metrics_path]:
            directory = os.path.dirname(path)
            os.makedirs(directory, exist_ok=True)

    def initiate_model_trainig(self):
        try:
            logging.info("Initiating model training")

            # load the transformed data
            transformed_data = pd.read_csv(self.config.transformed_data_path)

            # split the data into input and output
            logging.info("Splitting the data into input and output")
            X = transformed_data.drop(columns=['Heating_Load', 'Cooling_Load'], axis=1)
            y1 = transformed_data['Heating_Load']
            y2 = transformed_data['Cooling_Load']
            logging.info("Splitting completed")

            # split the data into train and test
            # for heating load
            logging.info("Splitting the data into train and test")
            X_train1, X_test1, y_train1, y_test1 = train_test_split(X, y1, test_size=0.2, random_state=42)
            # for cooling load
            X_train2, X_test2, y_train2, y_test2 = train_test_split(X, y2, test_size=0.2, random_state=42)
            logging.info("Splitting completed")

            # define the model
            model_1 = GradientBoostingRegressor(random_state=42)
            model_2 = GradientBoostingRegressor(random_state=42)

            # fit the model
            logging.info("Fitting the model")
            # for heating load
            model_1.fit(X_train1, y_train1)
            # for cooling load
            model_2.fit(X_train2, y_train2)
            logging.info("Fitting completed")

            # evaluate the model
            logging.info("Evaluating the model")
            # for heating load
            y_pred1 = model_1.predict(X_test1)
            # for cooling load
            y_pred2 = model_2.predict(X_test2)
            logging.info("Evaluation completed")

            # calculate the metrics
            logging.info("Calculating the metrics")
            # for heating load
            mse1 = mean_squared_error(y_test1, y_pred1)
            mae1 = mean_absolute_error(y_test1, y_pred1)
            r2_score1 = r2_score(y_test1, y_pred1)
            # for cooling load
            mse2 = mean_squared_error(y_test2, y_pred2)
            mae2 = mean_absolute_error(y_test2, y_pred2)
            r2_score2 = r2_score(y_test2, y_pred2)
            logging.info("Metrics calculated")

            # log the metrics
            logging.info("Metrics for heating load")
            logging.info("Mean Squared Error: %s", mse1)
            logging.info("Mean Absolute Error: %s", mae1)
            logging.info("R2 Score: %s", r2_score1)
            logging.info("Metrics for cooling load")
            logging.info("Mean Squared Error: %s", mse2)
            logging.info("Mean Absolute Error: %s", mae2)
            logging.info("R2 Score: %s", r2_score2)

            self.create_directories()

            # save the model
            logging.info("Saving the model and metrics")
            # for heating load
            save_object(model_1, self.config.model_path_1)
            # for cooling load
            save_object(model_2, self.config.model_path_2)

            # save the metrics
            metrics = {
                'heating': {
                    'mse': mse1,
                    'mae': mae1,
                    'r2_score': r2_score1
                },
                'cooling': {
                    'mse': mse2,
                    'mae': mae2,
                    'r2_score': r2_score2
                }
            }
            save_object(metrics, self.config.metrics_path)
            logging.info("Model and metrics saved successfully")

            logging.info("Model trained successfully")

            return (self.config.model_path_1, self.config.model_path_2, self.config.metrics_path)
        except Exception as e:
            logging.error("Error occurred while training model")
            raise CustomException(e,sys)