"""Compute Fingerprint"""
import numpy as np
import pandas as pd
import itertools as it

import rdkit
from rdkit import Chem, DataStructs
from rdkit.Chem import AllChem, MACCSkeys
from rdkit.Chem.Fingerprints import FingerprintMols
from rdkit.Chem.AtomPairs import Pairs

from modules.diversity_analysis.stats import statistical_values


class FP:
    def __init__(self, csv_name, fp_name):
        self.fp_name = fp_name[0]
        self.Data = pd.read_csv(f"generated_csv/{csv_name}", index_col="compound")
        if self.Data.shape[0] > 1001:
            print("data > 1001 componds")
            self.Data = self.Data.sample(2000, replace=True, random_state=1992)
        _ = ["Sequence", "Library"]
        self.ref = self.Data[_].as_matrix()
        self.diccionario = {
            "Atom Pair": self.atom_pair_fp(),
        }

    def atom_pair_fp(self):
        ms = [Chem.MolFromSmiles(i) for i in self.Data.SMILES]
        fp = [Pairs.GetAtomPairFingerprintAsBitVect(x) for x in ms]
        return fp

    def compute_similarity(self, df_fp, library):
        """
        return
        sim, array,  paired similarity
        y, array, cdf
        """
        fp = df_fp[df_fp["Library"] == library].fp
        sim = np.around(
            [
                DataStructs.FingerprintSimilarity(y, x)
                for x, y in it.combinations(fp, 2)
            ],
            decimals=2,
        )
        sim.sort()
        y = np.arange(1, len(sim) + 1) / len(sim)  # eje y
        y = np.around(y, decimals=2)
        return sim, y

    def similarity(self, fp_name):
        """
        Output
        result, DF with similarity coordinates
        stats, similarity stats of numerated libraries
        """
        fp_name = fp_name[0].replace(" ", "")
        # compute fp
        fp = self.diccionario[self.fp_name]
        df_fp = pd.DataFrame.from_dict({"fp": fp, "Library": self.Data.Library})
        # compute similarity
        sim_linear, y_linear = self.compute_similarity(df_fp, "linear")
        sim_cyclic, y_cyclic = self.compute_similarity(df_fp, "cyclic")
        # ref id
        lib_linear = np.asarray(["linear" for i in range(len(sim_linear))])
        lib_cyclic = np.asarray(["cyclic" for i in range(len(sim_cyclic))])
        pep_result = {
            "sim": np.concatenate((sim_linear, sim_cyclic), axis=0),
            "y": np.concatenate((y_linear, y_cyclic), axis=0),
            "Library": np.concatenate((lib_linear, lib_cyclic), axis=0),
        }
        pep_result = pd.DataFrame.from_dict(pep_result)
        ref_data = pd.read_csv(
            f"modules/similarity_db/coor_similatiry_reference_libraries_{fp_name}.csv",
            index_col="Unnamed: 0",
        )
        frames = [pep_result, ref_data]
        result = pd.concat(frames, axis=0).reset_index()
        stats = statistical_values(pep_result, fp_name)
        return result, stats
