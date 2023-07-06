import os
import sys
from src.logger import logging
from src.exception import CustomException
import pickle

# helper function to save object
def save_object(obj, filename):
    try:
        dir_path = os.path.dirname(filename)
        os.makedirs(dir_path, exist_ok=True)
        with open(filename, 'wb') as output:  # Overwrites any existing file.
            pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)
    except Exception as e:
        raise CustomException(e, error_detail=sys)
    
# helper function to load object
def load_object(filename):
    try:
        with open(filename, 'rb') as input:
            obj = pickle.load(input)
        return obj
    except Exception as e:
        raise CustomException(e, error_detail=sys)