import pandas as pd
from modules.ppi_chemical_space.compute_ecfp6 import ECFP6
# local execution
# from compute_ecfp6 import ECFP6

def get_test_molecule_data(smiles) -> pd.DataFrame:
    initial_data = {
        "SMILES": [smiles],
        "Library": [
            "Test Compound",
        ],
        "chembl_id": [
            "",
        ],
    }
    df1 = pd.DataFrame.from_dict(initial_data)
    test_data = ECFP6(smiles).explicit_descriptor()
    df2 = pd.DataFrame(data=test_data,
                        columns = [str(i) for i in range(2048)]
                    )
    result = pd.concat([df1, df2], axis=1)
    return result
