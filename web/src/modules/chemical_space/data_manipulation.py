import pandas as pd
import numpy as np
from pyparsing import col


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
    def id_columns_numerated(self):
        id_columns = [
            "Library",
            "SMILES",
            "Sequence",
        ]
        return id_columns

    @property
    def pc_columns(self):
        columns = [
            "PC 1",
            "PC 2",
            "PC 3",
            "PC 4",
            "PC 5",
            "PC 6",
        ]
        return columns

    @property
    def pca_result_columns(self):
        columns = [
            "Library",
            "SMILES",
            "chembl_id",
            "PC 1",
            "PC 2",
            "PC 3",
            "PC 4",
            "PC 5",
            "PC 6",
        ]
        return columns

    @property
    def tsne_result_columns(self):
        columns = [
            "Library",
            "SMILES",
            "chembl_id",
            "PC 1",
            "PC 2",
        ]
        return columns

    @property
    def molecular_descriptors(self):
        molecular_descriptor = ["HBA", "HBD", "RB", "LOGP", "TPSA", "MW"]
        return molecular_descriptor

    def merge_libraries_ecfp6(self, root, csv_name):
        """Merge numerated libraries with reference libraries"""
        numerated_libraries = pd.read_csv(
            f"{root}/generated_csv/{csv_name}",
            index_col=False,
        )
        numerated_libraries = numerated_libraries[self.id_columns_numerated]
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

    def merge_libraries_descriptors(self, root, csv_name):
        """Merge numerated libraries with reference libraries"""
        numerated_libraries = pd.read_csv(
            f"{root}/generated_csv/{csv_name}",
            index_col=False,
        )
        numerated_libraries = numerated_libraries.drop(["compound"], axis=1)
        numerated_libraries = numerated_libraries.rename(
            columns={
                "SMILES": "SMILES",
                "Library": "Library",
                "Sequence": "chembl_id",
                "HBA": "HBA",
                "HBD": "HBD",
                "RB": "RB",
                "LOGP": "LOGP",
                "TPSA": "TPSA",
                "MW": "MW",
            }
        )
        r_filename = "reference_database_descriptors.csv"
        reference_libraries = pd.read_csv(
            f"{root}/modules/{r_filename}", index_col="Unnamed: 0", low_memory=False
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
