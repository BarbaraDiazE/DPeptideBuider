"""
perform tSNE analysis
"""

import pandas as pd
import numpy as np

import sklearn
from sklearn import datasets, decomposition
from sklearn.manifold import TSNE


class performTSNE:
    def __init__(self, root, input_file, target, id_columns, smiles):
        data = pd.read_csv(f"{root}/modules/{input_file}", low_memory=False)
        test_df = get_test_molecule_data(smiles)
        print(test_df.head())
        self.data = pd.concat([data, test_df], axis=0)
        self.id_columns = id_columns
        print(self.data.head())
        print("Libraries are: ", self.data.Library.unique())
        print("Total compounds: ", self.data.shape[0])
        self.target = target
        self.root = root

    def get_numerical_data(self):
        descriptors = self.data.columns.to_list()
        for i in self.id_columns:
            descriptors.remove(i)
        numerical_data = self.data[descriptors]
        return numerical_data

    def get_id_data(self):
        return self.data[self.id_columns]

    def tsne_fingerprint(self):
        numerical_data = self.get_numerical_data()
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
        print("line 53")
        print(tsne_result.head(2))
        # _ = ["SMILES", "Sequence", "Library"]
        id_data = self.get_id_data()
        result = np.concatenate([id_data, tsne_result], axis=1)
        # result = pd.DataFrame(
        # data=result, columns=["PC 1", "PC 2", "SMILES", "Sequence", "Library"]
        # )
        print("line 59")
        print(result.head())
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
