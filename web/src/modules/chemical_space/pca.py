"""
Perform PCA analysis
"""

import pandas as pd
import numpy as np

import sklearn
from sklearn import datasets, decomposition
from sklearn.preprocessing import StandardScaler


class performPCA:
    def __init__(self):
        self.columns = ["PC 1", "PC 2", "PC 3", "PC 4", "PC 5", "PC 6"]

    def pca_descriptors(self, csv_name):
        """
        output
            result: Data Frame with PCA result, 
            a, variance PC 1
            b, variance PC 2
        """
        numerated_libraries = pd.read_csv(
            f"/src/generated_csv/{csv_name}", index_col="compound"
        )
        reference_libraries = pd.read_csv(
            "modules/reference_libraries.csv", index_col="Unnamed: 0"
        )
        Data = pd.concat([numerated_libraries, reference_libraries], axis=0)
        Data = Data.reset_index()
        feature_names = [
            "HBA",
            "HBD",
            "RB",
            "LOGP",
            "TPSA",
            "MW",
        ]  # configure manual if necessary
        _ = ["SMILES", "Sequence", "Library"]
        ref = Data[_]
        numerical_data = pd.DataFrame(
            StandardScaler().fit_transform(Data[feature_names])
        )
        sklearn_pca = sklearn.decomposition.PCA(
            n_components=6, svd_solver="full", whiten=True
        )
        model = sklearn_pca.fit(numerical_data)
        pca_result = pd.DataFrame(
            model.transform(numerical_data),
            columns=self.columns,
        )
        result = pd.concat([pca_result, ref], axis=1)
        a = round(list(model.explained_variance_ratio_)[0] * 100, 2)
        b = round(list(model.explained_variance_ratio_)[1] * 100, 2)
        return result, a, b

    def pca_fingerprint(self, fp_matrix, ref, fp_name):
        """
        output
            result: Data Frame with PCA result, 
            a, variance PC 1
            b, variance PC 2
        """
        # fp_name = fp_name[0].replace(" ", "")
        model = sklearn.decomposition.PCA(
            n_components=6, svd_solver="full", whiten=True
        ).fit(fp_matrix)
        pca_result = pd.DataFrame(
            model.transform(fp_matrix),
            columns=self.columns,
        )
        result = np.concatenate((pca_result, ref), axis=1)
        result = pd.DataFrame(
            data=result,
            columns=[
                "PC 1",
                "PC 2",
                "PC 3",
                "PC 4",
                "PC 5",
                "PC 6",
                "Sequence",
                "Library",
            ],
        )
        a = round(list(model.explained_variance_ratio_)[0] * 100, 2)
        b = round(list(model.explained_variance_ratio_)[1] * 100, 2)
        return result, a, b
