"""
Compute similarity from a database
"""

import numpy as np
import pandas as pd
import itertools as it

import rdkit    
from rdkit import Chem, DataStructs
from rdkit.Chem import AllChem, MACCSkeys
from rdkit.Chem.Fingerprints import FingerprintMols
from rdkit.Chem.AtomPairs import Pairs  

from compute_fingerprint import FP

def compute_similarity(fp):
        sim = [DataStructs.FingerprintSimilarity(y,x) for x,y in it.combinations(fp, 2)]
        sim = [ round(_, 2) for _ in sim ]
        #sim = [ round(_, 2) for _ in sim ]
        sim.sort()
        sim = np.asarray(sim) 
        y = np.arange(1, len(sim) + 1)/ len(sim) #eje y
        return sim, y


def maccskeys_fp(Data):
    ms=[Chem.MolFromSmiles(i) for i in Data.SMILES]
    fp = [MACCSkeys.GenMACCSKeys(x) for x in ms]
    return fp

def ecfp4_fp(Data):
    ms = [Chem.MolFromSmiles(i) for i in Data.SMILES]
    fp = [AllChem.GetMorganFingerprintAsBitVect(x,2) for x in ms]
    return fp

def ecfp6_fp(Data):
    ms=[Chem.MolFromSmiles(i) for i in Data.SMILES]
    fp = [AllChem.GetMorganFingerprintAsBitVect(x,3) for x in ms]
    return fp

def topological_fp(Data):
    ms =[Chem.MolFromSmiles(i) for i in Data.SMILES]
    fp = [FingerprintMols.FingerprintMol(x) for x in ms]
    return fp

def atom_pair_fp(Data):
    ms = [Chem.MolFromSmiles(i) for i in Data.SMILES]
    fp = [Pairs.GetAtomPairFingerprintAsBitVect(x) for x in ms]
    return fp

def ref_similarity(Data,  name, Library):
    _ = Data[Data["Library"] == Library]
    ###Updata function
    fp  = atom_pair_fp(_)
    print("ya calcule fp")
    #calcular similitud
    sim, y = compute_similarity(fp)
    print("ya calcule la similitud")
    #referencia 
    df_dict= {
        "sim": sim,
        "y": y,
        "Library": [Library for i in range(len(sim))],
    }
    df = pd.DataFrame.from_dict(df_dict)
    return df

Data = pd.read_csv('modules/reference_libraries.csv', index_col= "Unnamed: 0")
#print(Data.head())
print(Data.Library.unique())
DF_FDA = ref_similarity(Data, "Atom Pair", "FDA")
print("calcule FDA")
DF_FDA_PEP = ref_similarity(Data, "Atom Pair", "FDA PEP")
DF_MACRO = ref_similarity(Data, "Atom Pair", "MACRO")
DF_NP = ref_similarity(Data, "Atom Pair", "NP")
DF_PPI = ref_similarity(Data, "Atom Pair", "PPI")
frames = [DF_FDA, DF_FDA_PEP, DF_MACRO, DF_NP, DF_PPI]
df = pd.concat(frames, axis = 0)
df.reset_index()
print(df.head())
df.to_csv('modules/similatiry_reference_libraries_AtomPair.csv')
