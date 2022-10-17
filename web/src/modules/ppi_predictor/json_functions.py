import os
import json


def read_json(json_root, json_filename):
    f = open(os.path.join(json_root, json_filename))
    data_dict = json.load(f)
    return data_dict


def get_models_names():
    return read_json(f"{os.getcwd()}/modules/ppi_predictor", "models.json")


if __name__ == "__main__":
    x = get_models_names()
    print(x)
