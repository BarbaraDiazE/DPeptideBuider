"""
perform tSNE analysis from fingerprint representation data
"""

import pandas as pd
import numpy as np

import sklearn
from sklearn import datasets, decomposition
from sklearn.manifold import TSNE

from modules.ppi_chemical_space.ipp_molecule_data import get_test_molecule_data
# local execution
#from ipp_molecule_data import get_test_molecule_data


class TsneFP:
    def __init__(self, root, input_file, target, id_columns, smiles):
        data = pd.read_csv(f"{root}/modules/{input_file}", low_memory=False)
        test_df = get_test_molecule_data(smiles)
        self.data = pd.concat([data, test_df], axis=0)
        self.id_columns = id_columns
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
        id_data = self.get_id_data()
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
        algorithm_name = "t-SNE"
        return result, algorithm_name

# if __name__ == "__main__":
#     root_ = f"/home/babs/Documents/DIFACQUIM/DPeptideBuider/web/src/"
#     input_file_ = "reference_database_ecfp6.csv"
#     target = "library"
#     id_columns = [
#         "Library",
#         "SMILES",
#         "chembl_id",
#     ]
#     test_smiles = "CC(=O)NC1=CC=C(C=C1)O"
#     tsne = TsneFP(root_, input_file_, target, id_columns, test_smiles)
#     result, a_name = tsne.tsne_fingerprint()
#     print(result.head())    
#     print(result.shape)    
#     print       