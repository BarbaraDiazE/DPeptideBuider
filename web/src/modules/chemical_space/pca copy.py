"""
File to perform PCA
"""

import pandas as pd
import numpy as np
from decimal import Decimal

#import sklearn
import sklearn
from sklearn import datasets, decomposition
from sklearn.preprocessing import StandardScaler


class PCA:

    def __init__(self, csv_name):
        numerated_libraries = pd.read_csv(f'generated_csv/{csv_name}', index_col= "Unnamed: 0")
        reference_libraries = pd.read_csv('modules/reference_libraries.csv', index_col= "Unnamed: 0")
        Data = pd.concat([numerated_libraries, reference_libraries], axis = 0)
        self.Data = Data.reset_index()
        _ = ["SMILES", "Sequence", "Library"]
        self.ref_DF = self.Data[_]
        
    def pca_descriptors(self):
        feature_names = ["HBA", "HBD", "RB", "LOGP","TPSA", "MW"] #configure manual if necessary
        numerical_data = self.Data[feature_names]
        #normalize
        numerical_data = pd.DataFrame(StandardScaler().fit_transform(numerical_data))
        # Perform the PCA
        sklearn_pca = sklearn.decomposition.PCA(n_components=6, svd_solver = "full", whiten = True)
        model = sklearn_pca.fit(numerical_data)
        pca_result = pd.DataFrame(sklearn_pca.transform(numerical_data), columns=['PC 1','PC 2',"PC 3", 'PC 4','PC 5',"PC 6"])
        result = pd.concat([pca_result, self.ref_DF], axis = 1)
        #variance = list(model.explained_variance_ratio_)
        print(result.Library.unique())
        #self.a = round(variance[0] * 100, 2)
        #self.b = round(variance[1] * 100, 2)
        return result, model
