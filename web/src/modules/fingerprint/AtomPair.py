"""
Compute bit count matrix
"""
import pandas as pd
import numpy as np

import rdkit
from rdkit import Chem, DataStructs
from rdkit.Chem.AtomPairs import Pairs


def fp_matrix(fp):
    matrix_fp = []
    for f in fp:
        arr = np.zeros((1,))
        DataStructs.ConvertToNumpyArray(f, arr)
        matrix_fp.append(arr)
    return matrix_fp


class Bit_Count:
    def __init__(self, csv_name, fp_name):
        self.fp_name = fp_name[0]
        ref_comp = pd.read_csv(
            f"modules/reference_libraries.csv", index_col="Unnamed: 0"
        )
        peps = pd.read_csv(f"generated_csv/{csv_name}", index_col="compound")
        if peps.shape[0] > 1000:
            peps = peps.sample(n=1000, replace=True, random_state=1992)
        data = pd.concat([ref_comp, peps], axis=0)
        # data = data.sample(frac=0.3, replace=True, random_state=1992)
        self.data = data
        self.diccionario = {
            "ECFP 6": self.ecfp6(),
            "Atom Pairs": self.atom_pairs(),
        }

    def atom_pairs(self):
        ms = np.array([Chem.MolFromSmiles(i) for i in self.data.SMILES])
        # compute Atom Pair
        fp = [
            Pairs.GetAtomPairFingerprint(Chem.RemoveHs(x)).GetNonzeroElements()
            for x in ms
        ]
        # obtain all bits present
        bits_ap = set()
        for i in fp:
            bits_ap.update([*i])  # add bits for each molecule
        bits_ap = sorted(bits_ap)
        feature_matrix = list()
        # convert fp to bits
        for item in fp:
            vect_rep = np.isin(
                bits_ap, [*item]
            )  # vect_rep, var that indicates bits presents
            # identify axis to replace
            ids_to_update = np.where(vect_rep == True)
            vect_rep = 1 * vect_rep
            vect_rep = np.array(vect_rep).astype(int)
            # replace indices with bict values
            vect_rep[ids_to_update] = list(item.values())
            feature_matrix.append(vect_rep)
        return feature_matrix

    def ecfp6(self):
        ms = np.array([Chem.MolFromSmiles(i) for i in self.data.SMILES])
        fp = [Chem.AllChem.GetMorganFingerprintAsBitVect(x, 3) for x in ms]
        feature_matrix = fp_matrix(fp)
        return feature_matrix

    def feature_matrix(self, fp_name):
        feature_matrix = self.diccionario[self.fp_name]
        features = ["Sequence", "Library"]
        ref_id = self.data[features].as_matrix()
        return feature_matrix, ref_id
