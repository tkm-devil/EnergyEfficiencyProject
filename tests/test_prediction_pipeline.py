import unittest
import pandas as pd
from src.pipelines.prediction_pipeline import PredictionPipeline

class TestPredictionPipeline(unittest.TestCase):
    
    def setUp(self):
        self.pipeline = PredictionPipeline()
        self.df = pd.DataFrame({
            'Relative_Compactness': [0.75],
            'Surface_Area': [800],
            'Wall_Area': [250],
            'Roof_Area': [200],
            'Overall_Height': [3.5],
            'Orientation': ['2'],
            'Glazing_Area': [0.2],
            'Glazing_Area_Distribution': ['3']
        })

    def test_load_preprocessor(self):
        preprocessor = self.pipeline.load_preprocessor()
        self.assertIsNotNone(preprocessor)

    def test_apply_preprocessor(self):
        preprocessor = self.pipeline.load_preprocessor()
        preprocessed_df = self.pipeline.apply_preprocessor(self.df, preprocessor)
        self.assertIsNotNone(preprocessed_df)
        self.assertEqual(len(preprocessed_df), len(self.df))
        # Add more assertions to validate the preprocessed data if necessary

    def test_load_model(self):
        heating_load_model, cooling_load_model = self.pipeline.load_model()
        self.assertIsNotNone(heating_load_model)
        self.assertIsNotNone(cooling_load_model)

    def test_predict_heating_load(self):
        preprocessor = self.pipeline.load_preprocessor()
        preprocessed_df = self.pipeline.apply_preprocessor(self.df, preprocessor)
        heating_load_model, _ = self.pipeline.load_model()
        heating_load = self.pipeline.predict_heating_load(preprocessed_df, heating_load_model)
        self.assertIsNotNone(heating_load)
        self.assertEqual(len(heating_load), len(self.df))

    def test_predict_cooling_load(self):
        preprocessor = self.pipeline.load_preprocessor()
        preprocessed_df = self.pipeline.apply_preprocessor(self.df, preprocessor)
        _, cooling_load_model = self.pipeline.load_model()
        cooling_load = self.pipeline.predict_cooling_load(preprocessed_df, cooling_load_model)
        self.assertIsNotNone(cooling_load)
        self.assertEqual(len(cooling_load), len(self.df))

    def test_predict_results(self):
        heating_load, cooling_load = self.pipeline.predict_results(self.df)
        self.assertIsNotNone(heating_load)
        self.assertIsNotNone(cooling_load)
        self.assertEqual(len(heating_load), len(self.df))
        self.assertEqual(len(cooling_load), len(self.df))
        # Add more assertions to validate the prediction results if necessary

if __name__ == '__main__':
    unittest.main()

# Run the tests
# python -m unittest tests\test_prediction_pipeline.py

# Output
# .....
# ----------------------------------------------------------------------
# Ran 6 tests in 1.583s
# OK