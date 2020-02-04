"""
perform tSNE analysis
"""

import pandas as pd
import numpy as np

import sklearn
from sklearn import datasets, decomposition
from sklearn.manifold import TSNE

class performTSNE:
    
    def __init__(self):
        pass
            
    def tsne_descriptors(self, csv_name):
        """
        Input:
            csv_name : session csv_name
        Output:
            result: DataFrame whit tSNE result
        """
        numerated_libraries = pd.read_csv(f'generated_csv/{csv_name}', index_col= "Unnamed: 0")
        if numerated_libraries.shape[0] > 1001:
            numerated_libraries = numerated_libraries.sample(500, replace=True, random_state=1992)
        reference_libraries = pd.read_csv(f'modules/reference_libraries.csv', index_col= "Unnamed: 0")
        reference_libraries = reference_libraries.sample(frac=0.1, replace=True, random_state=1992)
        Data = pd.concat([numerated_libraries, reference_libraries], axis = 0)
        Data = Data.reset_index()
        _ = ["SMILES", "Sequence", "Library"]
        ref = Data[_]
        feature_names = ["HBA", "HBD", "RB", "LOGP","TPSA", "MW"] #configure manual if necessary
        model = TSNE(n_components=2,
                        init='pca',
                        random_state=1992, 
                        angle = 0.3,
                        perplexity=30
                        ).fit_transform(Data[feature_names])
        result = pd.DataFrame(data = model, columns=["PC 1","PC 2"])
        result = pd.concat([result, ref], axis = 1)
        return result, model

    def tsne_fingerprint(self, fp_matrix,  ref, fp_name):
        fp_name = fp_name[0].replace(' ', '')
        reference_libraries = pd.read_csv(f'modules/reference_libraries_{fp_name}.csv', index_col= "Unnamed: 0")
        reference_libraries = reference_libraries.sample(frac=0.1, replace=True, random_state=1992)
        #print(reference_libraries)
        reference = reference_libraries.select_dtypes(exclude=['object']).as_matrix()
        numerical = np.concatenate((fp_matrix, reference), axis = 0)
        model = TSNE(n_components=2,
                        init='pca',
                        random_state=1992, 
                        angle = 0.3,
                        perplexity=30
                        ).fit_transform(numerical)
        result = pd.DataFrame(data = model, columns=["PC 1","PC 2"])
        ref_libraries = reference_libraries.select_dtypes(include=['object']).as_matrix()
        ref_final = np.concatenate((ref, ref_libraries), axis = 0)
        result = np.concatenate((result, ref_final), axis = 1)
        result = pd.DataFrame(data=result, columns = ["PC 1", "PC 2", "Sequence", "Library"])
        return result