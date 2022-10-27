import pandas as pd
import numpy as np

class DataManipulation:

    def __init__(self):
        pass

    @property
    def id_columns(self):
        id_columns = [
            "Library",
            "SMILES",
            "chembl_id",
        ]
        return id_columns
            
    @property
    def molecular_descriptors(self):
        molecular_descriptor = ["HBA", "HBD", "RB", "LOGP", "TPSA", "MW"]
        return molecular_descriptor

    def merge_libraries_ecfp6(self, root, csv_name):
        """Merge numerated libraries with reference libraries"""
        numerated_libraries = pd.read_csv(
            f"{root}/generated_csv/{csv_name}",
            # index_col="compound"
            index_col=False,
        )
        numerated_libraries = numerated_libraries[["SMILES", "Library", "Sequence"]]
        numerated_libraries = numerated_libraries.rename(
            columns={"SMILES": "SMILES", "Library": "Library", "Sequence": "chembl_id"}
        )
        numerated_libraries = self.feature_matrix(numerated_libraries)
        r_filename = "reference_database_ecfp6.csv"
        reference_libraries = pd.read_csv(
            f"{root}/modules/{r_filename}", low_memory=False
        )
        data = pd.concat(
            [numerated_libraries, reference_libraries], axis=0, ignore_index=True
        )
        return data

    def get_id_data(self, data):
        return data[self.id_columns]    

    def get_numerical_data_fp(self, data) -> pd.DataFrame:
        descriptors = data.columns.to_list()
        for i in self.id_columns:
            descriptors.remove(i)
        numerical_data = data[descriptors]
        return numerical_data    