import numpy as np

from rdkit import Chem, DataStructs
from rdkit.Chem import AllChem


class ECFP6:
    def __init__(self, smiles: str):
        self.smiles = smiles

    def get_ecfp6(self) -> list:
        ms = [Chem.MolFromSmiles(self.smiles)]
        fp = [AllChem.GetMorganFingerprintAsBitVect(x, 3) for x in ms]
        return fp

    def explicit_descriptor(self) -> np.array:
        fp = self.get_ecfp6()
        output = []
        for f in fp:
            arr = np.zeros((1,))
            DataStructs.ConvertToNumpyArray(f, arr)
            output.append(arr)
        return np.asarray(output)
