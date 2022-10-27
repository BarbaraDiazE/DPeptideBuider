"""
perform tSNE analysis for DPeptideChemical Space
"""

from re import T
import pandas as pd
import numpy as np

import sklearn
from sklearn import datasets, decomposition
from sklearn.manifold import TSNE


# local execution
from ecfp6 import BitCount
from data_manipulation import DataManipulation


class performTSNE(DataManipulation, BitCount):
    def __init__(self):
        pass

    def tsne_descriptors(self, csv_name):
        """
        Input:
            csv_name : session csv_name
        Output:
            result: DataFrame whit tSNE result
        """
        numerated_libraries = pd.read_csv(
            f"/src/generated_csv/{csv_name}", index_col="compound"
        )
        if numerated_libraries.shape[0] > 1001:
            numerated_libraries = numerated_libraries.sample(
                500, replace=True, random_state=1992
            )
        ref_data = pd.read_csv(
            f"modules/reference_libraries.csv", index_col="Unnamed: 0"
        )
        ref_data = ref_data.sample(frac=0.2, replace=True, random_state=1992)
        data = pd.concat([numerated_libraries, ref_data], axis=0).reset_index()
        data = data.drop(["index"], axis=1)
        features = ["HBA", "HBD", "RB", "LOGP", "TPSA", "MW"]
        model = TSNE(
            n_components=2,
            init="pca",
            random_state=1992,
            angle=0.3,
            perplexity=30,
            n_iter=1000,
            n_jobs=6,
        ).fit_transform(data[features].values)
        tsne_result = np.array(model)
        _ = ["SMILES", "Sequence", "Library"]
        total_id = data[_].values
        result = np.concatenate((tsne_result, total_id), axis=1)
        result = pd.DataFrame(
            data=result, columns=["PC 1", "PC 2", "SMILES", "Sequence", "Library"]
        )
        return result

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
        result = pd.DataFrame(
            data=result,
            columns=[
                "Library",
                "SMILES",
                "chembl_id",
                "PC 1",
                "PC 2",
            ],
        )
        print(result.head(2))
        print(result.iloc[0])
        return result


if __name__ == "__main__":
    # Define variables
    root_ = f"/home/babs/Documents/DIFACQUIM/DPeptideBuider/web/src"
    filename = "database_20221017_154321.csv"
    pca = performTSNE()
    result = pca.tsne_fingerprint(root_, filename)
