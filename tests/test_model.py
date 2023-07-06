import unittest
import pandas as pd
import os
import pickle

class ModelTest(unittest.TestCase):
    def setUp(self):
        # Get the current directory
        current_dir = os.getcwd()

        # Define the paths relative to the current directory
        preprocessor_path = os.path.join(current_dir, 'artifacts', 'models', 'preprocessor.pkl')
        heating_load_model_path = os.path.join(current_dir, 'artifacts', 'models', 'heating_load_model.pkl')
        cooling_load_model_path = os.path.join(current_dir, 'artifacts', 'models', 'cooling_load_model.pkl')

        # Load the preprocessor
        with open(preprocessor_path, 'rb') as f:
            self.preprocessor = pickle.load(f)

        # Load the models
        with open(heating_load_model_path, 'rb') as f:
            self.heating_load_model = pickle.load(f)
        with open(cooling_load_model_path, 'rb') as f:
            self.cooling_load_model = pickle.load(f)

    def test_preprocessor(self):
        # Sample input data
        data = {
            'Relative_Compactness': [0.8],
            'Surface_Area': [700],
            'Wall_Area': [250],
            'Roof_Area': [150],
            'Overall_Height': [5.0],
            'Orientation': [2],
            'Glazing_Area': [0.25],
            'Glazing_Area_Distribution': [3]
        }
        df = pd.DataFrame(data)

        # Transform the DataFrame using the preprocessor
        df_preprocessed = self.preprocessor.transform(df)

        # Check if the preprocessed DataFrame has the expected shape
        self.assertEqual(df_preprocessed.shape, (1, 8), "Unexpected shape of preprocessed DataFrame")

        # Check if the column names of the preprocessed DataFrame match the expected names
        expected_column_names = ['preprocessor__Relative_Compactness', 'preprocessor__Surface_Area',
                                'preprocessor__Wall_Area', 'preprocessor__Roof_Area',
                                'preprocessor__Overall_Height', 'preprocessor__Orientation',
                                'preprocessor__Glazing_Area', 'preprocessor__Glazing_Area_Distribution']
        df_preprocessed = pd.DataFrame(df_preprocessed, columns=expected_column_names)
        self.assertListEqual(list(df_preprocessed.columns), expected_column_names, "Column names do not match the preprocessor")

    def test_model_prediction(self):
        # Sample input data
        data = {
            'Relative_Compactness': [0.9],
            'Surface_Area': [563.5],
            'Wall_Area': [318.5],
            'Roof_Area': [122.5],
            'Overall_Height': [7.0],
            'Orientation': [2],
            'Glazing_Area': [0.0],
            'Glazing_Area_Distribution': [0]
        }
        df = pd.DataFrame(data)

        # Transform the DataFrame using the preprocessor
        df_preprocessed = self.preprocessor.transform(df)

        # Predict heating load
        heating_load = self.heating_load_model.predict(df_preprocessed)

        # Assert that the predicted heating load has the expected value or range
        expected_heating_load = 20.84  # Provide your expected value or range here
        self.assertAlmostEqual(heating_load[0], expected_heating_load, delta=0.5)

        # Predict cooling load
        cooling_load = self.cooling_load_model.predict(df_preprocessed)

        # Assert that the predicted cooling load has the expected value or range
        expected_cooling_load = 28.28  # Provide your expected value or range here
        self.assertAlmostEqual(cooling_load[0], expected_cooling_load, delta=0.5)

if __name__ == '__main__':
    unittest.main()

# Run the tests
# python -m unittest tests\test_model.py

# Output:
# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 1.634s
#
# OK