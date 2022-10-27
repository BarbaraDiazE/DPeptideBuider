"""
Compute ECFP6 extended matrix
"""
import numpy as np
import pandas as pd
import rdkit
from rdkit import Chem
from rdkit.Chem import AllChem, DataStructs


import itertools as it


def fp_matrix(fp) -> np.array:
    matrix_fp = []
    for f in fp:
        arr = np.zeros((1,))
        DataStructs.ConvertToNumpyArray(f, arr)
        matrix_fp.append(arr)
    return matrix_fp


class BitCount:
    def __init__(self):
        pass

    def ecfp6(self, data: pd.DataFrame):
        ms = np.array([Chem.MolFromSmiles(i) for i in data.SMILES])
        fp = [Chem.AllChem.GetMorganFingerprintAsBitVect(x, 3) for x in ms]
        feature_matrix = fp_matrix(fp)
        return feature_matrix

    def feature_matrix(self, data: pd.DataFrame):
        feature_matrix = self.ecfp6(data)
        id_ = ["SMILES", "Library", "chembl_id"]
        id_data = data[id_]
        fp_data = pd.DataFrame(
            data=feature_matrix, columns=[str(i) for i in range(2048)]
        )
        output_data = pd.concat([id_data, fp_data], axis=1)
        return output_data
