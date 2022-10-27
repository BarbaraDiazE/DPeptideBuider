"""
Perform PCA analysis
"""

import pandas as pd
import numpy as np

import sklearn
from sklearn import datasets, decomposition
from sklearn.preprocessing import StandardScaler

# local
from ecfp6 import BitCount


class performPCA(BitCount):
    def __init__(self):
        self.columns = ["PC 1", "PC 2", "PC 3", "PC 4", "PC 5", "PC 6"]

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

    @property
    def molecular_descriptors(self):
        molecular_descriptor = ["HBA", "HBD", "RB", "LOGP", "TPSA", "MW"]
        return molecular_descriptor

    @property
    def id_columns(self):
        id_columns = [
            "Library",
            "SMILES",
            "chembl_id",
        ]
        return id_columns

    def pca_descriptors(self):
        """
        output
            result: Data Frame with PCA result,
            a, variance PC 1
            b, variance PC 2
        """
        feature_names = self.molecular_descriptors  # configure manual if necessary
        # _ = ["SMILES", "Sequence", "Library"]
        # ref = Data[_]
        # numerical_data = pd.DataFrame(
        # StandardScaler().fit_transform(Data[feature_names])
        # )
        # sklearn_pca = sklearn.decomposition.PCA(
        # n_components=6, svd_solver="full", whiten=True
        # )
        # model = sklearn_pca.fit(numerical_data)
        # pca_result = pd.DataFrame(
        # model.transform(numerical_data),
        # columns=self.columns,
        # )
        # result = pd.concat([pca_result, ref], axis=1)
        # a = round(list(model.explained_variance_ratio_)[0] * 100, 2)
        # b = round(list(model.explained_variance_ratio_)[1] * 100, 2)
        # return result, a, b

    def get_numerical_data(self):
        descriptors = self.data.columns.to_list()
        for i in self.id_columns:
            descriptors.remove(i)
        numerical_data = self.data[descriptors]
        return numerical_data

    def get_id_data(self, data):
        return data[self.id_columns]

    def get_numerical_data_fp(self, data) -> pd.DataFrame:
        descriptors = data.columns.to_list()
        for i in self.id_columns:
            descriptors.remove(i)
        numerical_data = data[descriptors]
        return numerical_data

    def pca_fingerprint(self, root, csv_name):
        """
        output
            result: Data Frame with PCA result,
            a, variance PC 1
            b, variance PC 2
        """
        fp_data = self.merge_libraries_ecfp6(root, csv_name)
        numerical_data = self.get_numerical_data_fp(fp_data)
        model = sklearn.decomposition.PCA(
            n_components=6, svd_solver="full", whiten=True
        ).fit(numerical_data)
        pca_result = pd.DataFrame(
            model.transform(numerical_data),
            columns=self.columns,
        )
        a = round(list(model.explained_variance_ratio_)[0] * 100, 2)
        b = round(list(model.explained_variance_ratio_)[1] * 100, 2)
        id_data = self.get_id_data(fp_data)
        result = np.concatenate((id_data, pca_result), axis=1)
        result = pd.DataFrame(
            data=result,
            columns=[
                "Library",
                "SMILES",
                "chembl_id",
                "PC 1",
                "PC 2",
                "PC 3",
                "PC 4",
                "PC 5",
                "PC 6",
            ],
        )
        a = round(list(model.explained_variance_ratio_)[0] * 100, 2)
        b = round(list(model.explained_variance_ratio_)[1] * 100, 2)
        algorithm_name = "PCA"
        print("line 83, si me ejecuto")
        return result, a, b, algorithm_name


if __name__ == "__main__":
    # Define variables
    root_ = f"/home/babs/Documents/DIFACQUIM/DPeptideBuider/web/src"
    filename = "database_20221017_154321.csv"
    pca = performPCA()
    result, a, b, al = pca.pca_fingerprint(root_, filename)
    print(a, b)
