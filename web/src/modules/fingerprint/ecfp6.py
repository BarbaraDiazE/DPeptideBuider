"""
Compute bit count matrix
"""
import pandas as pd
import numpy as np

import rdkit
from rdkit import Chem, DataStructs



def fp_matrix(fp) -> np.array:
    matrix_fp = []
    for f in fp:
        arr = np.zeros((1,))
        DataStructs.ConvertToNumpyArray(f, arr)
        matrix_fp.append(arr)
    return matrix_fp


class BitCount:
    def __init__(self, csv_name, fp_name):
        self.fp_name = fp_name[0]
        ref_comp = pd.read_csv(
            f"modules/reference_libraries_{fp_name.lower()}.csv", index_col="Unnamed: 0"
        )
        print(ref_comp.head(2))
        peps = pd.read_csv(f"/src/generated_csv/{csv_name}", index_col="compound")
        if peps.shape[0] > 1000:
            peps = peps.sample(n=1000, replace=True, random_state=1992)
        data = pd.concat([ref_comp, peps], axis=0)
        # data = data.sample(frac=0.3, replace=True, random_state=1992)
        self.data = data
        self.diccionario = {
            "ECFP 6": self.ecfp6(),
        }


    def ecfp6(self):
        ms = np.array([Chem.MolFromSmiles(i) for i in self.data.SMILES])
        fp = [Chem.AllChem.GetMorganFingerprintAsBitVect(x, 3) for x in ms]
        feature_matrix = fp_matrix(fp)
        return feature_matrix

    def feature_matrix(self, fp_name: str):
        feature_matrix = self.diccionario[self.fp_name]
        features = ["Sequence", "Library"]
        ref_id = self.data[features].values
        return feature_matrix, ref_id
