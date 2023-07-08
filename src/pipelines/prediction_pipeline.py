# In this file we will completely automate the process of prediction of results for the users.
# Path: src\pipelines\prediction_pipeline.py

# import libraries
import pandas as pd
import pickle
import os
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object

current_dir = os.getcwd()


# create a PredictionPipeline class
class PredictionPipeline:

    def __init__(self):
        pass

    # load the preprocessor
    def load_preprocessor(self):
        try:
            logging.info("Loading preprocessor")
            preprocessor = load_object(os.path.join(current_dir,'artifacts', 'models', 'preprocessor.pkl'))
            logging.info("Loading preprocessor completed")
            return preprocessor
        except Exception as e:
            logging.error("Error occurred while loading preprocessor")
            raise CustomException("Error occurred while loading preprocessor", e)
        
    # apply the preprocessor
    def apply_preprocessor(self, df, preprocessor):
        try:
            logging.info("Applying preprocessor")
            column_names = ['Relative_Compactness', 'Surface_Area', 'Wall_Area', 'Roof_Area',
                            'Overall_Height', 'Orientation', 'Glazing_Area', 'Glazing_Area_Distribution']
            df.columns = column_names
            df_transformed = preprocessor.transform(df)
            df_transformed = pd.DataFrame(df_transformed, columns=column_names)
            logging.info("Applying preprocessor completed")
            return df_transformed
        except Exception as e:
            logging.error("Error occurred while applying preprocessor")
            raise CustomException("Error occurred while applying preprocessor", e)
        
    # load the model
    def load_model(self):
        try:
            logging.info("Loading models")
            # Load the heating load model
            heating_load_model = load_object(os.path.join(current_dir,'artifacts', 'models', 'heating_load_model.pkl'))

            # Load the cooling load model
            cooling_load_model = load_object(os.path.join(current_dir,'artifacts', 'models', 'cooling_load_model.pkl'))

            logging.info("Loading models completed")
            return heating_load_model, cooling_load_model
        except Exception as e:
            logging.error("Error occurred while loading models")
            raise CustomException("Error occurred while loading models", e)
        
    # predict heating load
    def predict_heating_load(self, df, heating_load_model):
        try:
            logging.info("Predicting heating load")
            return heating_load_model.predict(df)[0]
        except Exception as e:
            logging.error("Error occurred while predicting heating load")
            raise CustomException("Error occurred while predicting heating load", e)
        
    # predict cooling load
    def predict_cooling_load(self, df, cooling_load_model):
        try:
            logging.info("Predicting cooling load")
            return cooling_load_model.predict(df)[0]
        except Exception as e:
            logging.error("Error occurred while predicting cooling load")
            raise CustomException("Error occurred while predicting cooling load", e)
        
    # predict the results
    def predict_results(self, df):
        try:
            logging.info("Initiating prediction pipeline")
            preprocessor = self.load_preprocessor()
            df = self.apply_preprocessor(df, preprocessor)
            heating_load_model, cooling_load_model = self.load_model()
            heating_load = self.predict_heating_load(df, heating_load_model)
            cooling_load = self.predict_cooling_load(df, cooling_load_model)
            logging.info("Prediction pipeline completed")
            return heating_load, cooling_load
        except Exception as e:
            logging.error("Error occurred while predicting results")
            raise CustomException("Error occurred while predicting results", e)
