"""Compute Fingerprint"""
import numpy as np
import pandas as pd
import itertools as it
import multiprocessing as mp

import rdkit
from rdkit import Chem, DataStructs
from rdkit.Chem import AllChem, MACCSkeys
from rdkit.Chem.Fingerprints import FingerprintMols
from rdkit.Chem.AtomPairs import Pairs

from modules.diversity_analysis.stats import statistical_values


def get_smiles(i):
    return Chem.MolFromSmiles(i)


def atom_pairs(i):
    return Pairs.GetAtomPairFingerprintAsBitVect(i)


def paired_sim(i):
    return DataStructs.FingerprintSimilarity(i[0], i[1])


class FP:
    def __init__(self, csv_name, fp_name):
        self.fp_name = fp_name[0]
        self.Data = pd.read_csv(f"generated_csv/{csv_name}", index_col="compound")
        if self.Data.shape[0] > 500:
            self.Data = self.Data.sample(150, replace=True, random_state=1992)

    def atom_pair_fp(self):
        smiles = self.Data.SMILES
        pool = mp.Pool(mp.cpu_count())
        ms = pool.map(get_smiles, [item for item in smiles])
        pool.close()
        pool = mp.Pool(mp.cpu_count())
        fp = pool.map(atom_pairs, [item for item in ms])
        pool.close()
        return fp

    @staticmethod
    def compute_similarity(df_fp, library):
        """
        input
        df_fp, Dataframe (fingerprint, and library)
        library, str
        return
        sim, array,  paired similarity
        y, array, cdf
        """
        fp = df_fp[df_fp["Library"] == library].fp
        _ = list(it.combinations(fp, 2))
        # sim = np.around(
        #     [
        #         DataStructs.FingerprintSimilarity(y, x)
        #         for x, y in it.combinations(fp, 2)
        #     ],
        #     decimals=2,
        # )
        pool = mp.Pool(mp.cpu_count())
        sim = pool.map(paired_sim, [item for item in _])
        pool.close()
        sim = np.around(sim, decimals=3)
        sim.sort()
        l = len(sim)
        y = np.arange(1, l + 1) / l  # eje y
        y = np.around(y, decimals=3)
        return sim, y

    def similarity(self, fp_name):
        """
        Output
        result, DF with similarity coordinates
        stats, similarity stats of numerated libraries
        """
        fp_name = fp_name[0].replace(" ", "")
        # compute fp
        fp = self.atom_pair_fp()
        df_fp = pd.DataFrame.from_dict({"fp": fp, "Library": self.Data.Library})
        print("df_fp esta listo")
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
