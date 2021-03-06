"""
perform tSNE analysis
"""

import pandas as pd
import numpy as np

import sklearn
from sklearn import datasets, decomposition
from sklearn.manifold import TSNE


class performTSNE:
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
            f"generated_csv/{csv_name}", index_col="compound"
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
        ).fit_transform(data[features].as_matrix())
        tsne_result = np.array(model)
        _ = ["SMILES", "Sequence", "Library"]
        total_id = data[_].as_matrix()
        result = np.concatenate((tsne_result, total_id), axis=1)
        result = pd.DataFrame(
            data=result, columns=["PC 1", "PC 2", "SMILES", "Sequence", "Library"]
        )
        return result

    def tsne_fingerprint(self, fp_matrix, ref_id, fp_name):
        """
        Input:
            fp_matrix: explicit fingerprint of numerated libraries
            ref_id, id of numerated libraries and ref compounds
            fp_name, list, selected fp
        Output:
            result: DataFrame whit tSNE result
        """
        fp_name = fp_name[0].replace(" ", "")
        model = TSNE(
            n_components=2,
            init="pca",
            random_state=1992,
            angle=0.3,
            perplexity=30,
            n_iter=1000,
            n_jobs=6,
        ).fit_transform(fp_matrix)
        tsne_result = np.array(model)
        result = np.concatenate((tsne_result, ref_id), axis=1)
        result = pd.DataFrame(
            data=result, columns=["PC 1", "PC 2", "Sequence", "Library"]
        )
        return result
