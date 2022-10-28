"""
perform tSNE analysis for DPeptideChemical Space
"""

# from re import T
import pandas as pd
import numpy as np

import sklearn
from sklearn.manifold import TSNE

# django execution
from modules.chemical_space.ecfp6 import BitCount
from modules.chemical_space.data_manipulation import DataManipulation

# local execution
# from ecfp6 import BitCount
# from data_manipulation import DataManipulation


class performTSNE(DataManipulation, BitCount):
    def __init__(self):
        pass

    def tsne_descriptors(self, root: str, csv_name: str):
        descriptors_data = self.merge_libraries_descriptors(root, csv_name)
        numerical_data = self.get_numerical_data_fp(descriptors_data)
        model = TSNE(
            n_components=2,
            init="pca",
            random_state=1992,
            angle=0.3,
            perplexity=30,
            n_iter=1000,
            n_jobs=6,
        ).fit_transform(numerical_data)
        tsne_result = pd.DataFrame(
            data=np.array(model),
            columns=["PC 1", "PC2"],
        )
        tsne_result = tsne_result.round(2)
        id_data = self.get_id_data(descriptors_data)
        result = np.concatenate([id_data, tsne_result], axis=1)
        result = pd.DataFrame(data=result, columns=self.tsne_result_columns)
        algorithm_name = "t-SNE"
        return result, algorithm_name

    def tsne_fingerprint(self, root: str, csv_name: str):
        """
        Input:
            root:
            csv_name
        Output:
            result: DataFrame whit tSNE result
        """
        fp_data = self.merge_libraries_ecfp6(root, csv_name)
        numerical_data = self.get_numerical_data_fp(fp_data)
        model = TSNE(
            n_components=2,
            init="pca",
            random_state=1992,
            angle=0.3,
            perplexity=30,
            n_iter=1000,
            n_jobs=6,
        ).fit_transform(numerical_data)
        tsne_result = pd.DataFrame(
            data=np.array(model),
            columns=["PC 1", "PC2"],
        )
        tsne_result = tsne_result.round(2)
        id_data = self.get_id_data(fp_data)
        result = np.concatenate((id_data, tsne_result), axis=1)
        result = pd.DataFrame(data=result, columns=self.tsne_result_columns)
        algorithm_name = "t-SNE"
        return result, algorithm_name


if __name__ == "__main__":
    # Define variables
    root_ = f"/home/babs/Documents/DIFACQUIM/DPeptideBuider/web/src"
    filename = "database_20221017_154321.csv"
    pca = performTSNE()
    result, algorithm_name = pca.tsne_descriptors(root_, filename)
    print(result.iloc[0])
