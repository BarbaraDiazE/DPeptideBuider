import os
import joblib
import pandas as pd

from modules.descriptors.compute_descriptors import ECFP6
from modules.ppi_predictor.json_functions import get_models_names

# MODELS_PATH = os.getenv("MODELS_PATH")
MODELS_PATH = "/src/trained_models"

class PPIPrediction:
    def __init__(self, test_smiles):
        self.test_smiles = test_smiles

    @staticmethod
    def load_model(model_filename):
        return joblib.load(os.path.join(f"{MODELS_PATH}", model_filename))

    def test_data(self):
        try:
            test_data = ECFP6(self.test_smiles).explicit_descriptor()
        except Exception:
            test_data = "Please insert a valid structure"
        return test_data

    def prediction(self, model_filename):
        model = self.load_model(model_filename)
        test_data = self.test_data()
        try:
            y = model.predict(test_data)
            prediction = str()
            if y[0] == 0:
                prediction = "Inactive"
            elif y[0] == 1:
                prediction = "Active"
            print("line 36")
            print(prediction)
            return prediction
        except Exception:
            return "Please insert a valid structure"

    def activity_against_target(self):
        models_names = get_models_names()
        filter_prediction = self.prediction(models_names["filter"])
        if filter_prediction == "Active":
            target_predictions = {
                value: [self.prediction(f"ensemble_ecfp6_1_{key}.pkl")]
                for key, value in models_names.items()
                if "target" in key
            }
        elif filter_prediction == "Inactive":
            target_predictions = {
                value: ["Inactive"] for key, value in models_names.items() if "target" in key
            }
        else:
            target_predictions = {"": ["Insert a valid structure"]}
        target_predictions = pd.DataFrame.from_dict(target_predictions).transpose()
        target_predictions.columns = ["Prediction"]
        return target_predictions


def molecule_prediction(smiles: str):
    data = PPIPrediction(smiles).activity_against_target()
    print("## LINE 62 ##")
    return data
