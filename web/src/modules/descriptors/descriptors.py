import numpy as np
import pandas as pd
import multiprocessing as mp

import rdkit
from rdkit import Chem
from rdkit.Chem import Descriptors, MolToSmiles


def get_smiles(item):
    return Chem.MolFromSmiles(item)


def get_cann_smiles(mol):
    return Chem.MolToSmiles(mol)


def get_hbd(mol):
    return Descriptors.NumHDonors(mol)


def get_hba(mol):
    return Descriptors.NumHAcceptors(mol)


def get_rb(mol):
    return Descriptors.NumRotatableBonds(mol)


def get_logp(mol):
    return Descriptors.MolLogP(mol)


def get_tpsa(mol):
    return Descriptors.TPSA(mol)


def get_mw(mol):
    return Descriptors.MolWt(mol)


def compute_descriptors(smiles):
    print("soy los smiles que recibe compute descriptors", type(smiles), len(smiles))
    np_smiles = np.array(smiles)
    # smiles
    pool = mp.Pool(mp.cpu_count())
    smiles = pool.map(get_smiles, [x for x in np_smiles])
    pool.close()
    np_molecules = np.array(smiles)
    # CanonicalSmiles = list(map(lambda x: Chem.MolToSmiles(x), smiles))
    pool = mp.Pool(mp.cpu_count())
    CanonicalSmiles = pool.map(get_cann_smiles, [mol for mol in np_molecules])
    HBA = pool.map(get_hba, [mol for mol in np_molecules])
    HBD = pool.map(get_hbd, [mol for mol in np_molecules])
    RB = pool.map(get_rb, [mol for mol in np_molecules])
    LOGP = pool.map(get_logp, [mol for mol in np_molecules])
    TPSA = pool.map(get_tpsa, [mol for mol in np_molecules])
    MW = pool.map(get_mw, [mol for mol in np_molecules])
    pool.close()

    return CanonicalSmiles, HBA, HBD, RB, LOGP, TPSA, MW
