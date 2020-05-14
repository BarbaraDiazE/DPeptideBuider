"""
Atom Pair implementation 
"""
import pandas as pd
import numpy as np
import rdkit

from rdkit import Chem
from rdkit.Chem.AtomPairs import Pairs

"""
Compute atom pair bits
"""


def comp_fp(csv_name):
    # Data
    ref_comp = pd.read_csv(f"modules/reference_libraries.csv", index_col="Unnamed: 0")
    peps = pd.read_csv(f"generated_csv/{csv_name}", index_col="Unnamed: 0")
    data = pd.concat([ref_comp, peps], axis=0)
    data = data.sample(frac=0.3, replace=True, random_state=1992)
    ms = np.array([Chem.MolFromSmiles(i) for i in data.SMILES])
    # compute Atom Pair
    fp = [
        Pairs.GetAtomPairFingerprint(Chem.RemoveHs(x)).GetNonzeroElements() for x in ms
    ]
    # obtain all bits present
    bits_ap = set()
    for i in fp:
        bits_ap.update([*i])  # add bits for each molecule
    bits_ap = sorted(bits_ap)
    ap_result = list()
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
        ap_result.append(vect_rep)
    features = ["Sequence", "Library"]
    ref_id = data[features].as_matrix()
    return ap_result, ref_id
