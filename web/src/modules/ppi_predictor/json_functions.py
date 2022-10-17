import os
import json


def read_json(json_root: str, json_filename: str):
    f = open(os.path.join(json_root, json_filename))
    data_dict = json.load(f)
    return data_dict


def get_models_names():
    return read_json(f"{os.getcwd()}/modules/ppi_predictor", "models.json")

