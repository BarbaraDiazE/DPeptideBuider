"""
Perform PCA analysis for DpeptideChemical Space
"""

import pandas as pd
import numpy as np

import sklearn
from sklearn import datasets, decomposition
from sklearn.preprocessing import StandardScaler

# local execution
from ecfp6 import BitCount
from data_manipulation import DataManipulation


class performPCA(DataManipulation, BitCount):
    def __init__(self):
        super().__init__()

    def pca_descriptors(self, root: str, csv_name: str):
        descriptors_data = self.merge_libraries_descriptors(root, csv_name)
        numerical_data = self.get_numerical_data_fp(descriptors_data)
        model = sklearn.decomposition.PCA(
            n_components=6, svd_solver="full", whiten=True
        ).fit(numerical_data)
        pca_result = pd.DataFrame(
            data=model.transform(numerical_data),
            columns=self.pc_columns,
        )
        pca_result = pca_result.round(2)
        id_data = self.get_id_data(descriptors_data)
        result = np.concatenate([id_data, pca_result], axis=1)
        result = pd.DataFrame(data=result, columns=self.pca_result_columns)
        a = round(list(model.explained_variance_ratio_)[0] * 100, 2)
        b = round(list(model.explained_variance_ratio_)[1] * 100, 2)
        algorithm_name = "PCA"
        return result, a, b, algorithm_name

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
            columns=self.pc_columns,
        )
        pca_result = pca_result.round(2)
        a = round(list(model.explained_variance_ratio_)[0] * 100, 2)
        b = round(list(model.explained_variance_ratio_)[1] * 100, 2)
        id_data = self.get_id_data(fp_data)
        result = np.concatenate([id_data, pca_result], axis=1)
        result = pd.DataFrame(data=result, columns=self.pca_result_columns)
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
    result, a, b, al = pca.pca_descriptors(root_, filename)
    print(a, b)
