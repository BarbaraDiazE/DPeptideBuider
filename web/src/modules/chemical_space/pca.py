"""
Perform PCA analysis
"""

import pandas as pd
import numpy as np

import sklearn
from sklearn import datasets, decomposition
from sklearn.preprocessing import StandardScaler

class performPCA:

    def __init__(self):
        pass
        
    def pca_descriptors(self, csv_name):
        """
        output
            result: Data Frame with PCA result, 
            model: PCA Model
        """
        numerated_libraries = pd.read_csv(f'generated_csv/{csv_name}', index_col= "Unnamed: 0")
        reference_libraries = pd.read_csv('modules/reference_libraries.csv', index_col= "Unnamed: 0")
        Data = pd.concat([numerated_libraries, reference_libraries], axis = 0)
        Data = Data.reset_index()
        feature_names = ["HBA", "HBD", "RB", "LOGP","TPSA", "MW"] #configure manual if necessary
        _ = ["SMILES", "Sequence", "Library"]
        ref = Data[_]
        numerical_data = pd.DataFrame(StandardScaler().fit_transform(Data[feature_names]))
        sklearn_pca = sklearn.decomposition.PCA(n_components=6, svd_solver = "full", whiten = True)
        model = sklearn_pca.fit(numerical_data)
        pca_result = pd.DataFrame(model.transform(numerical_data), columns=['PC 1','PC 2',"PC 3", 'PC 4','PC 5',"PC 6"])
        result = pd.concat([pca_result, ref], axis = 1)
        #variance = list(model.explained_variance_ratio_)
        #self.a = round(variance[0] * 100, 2)
        #self.b = round(variance[1] * 100, 2)
        return result, model

    def pca_fingerprint(self, fp_matrix, ref, fp_name):
        fp_name = fp_name[0].replace(' ', '')
        reference_libraries = pd.read_csv(f'modules/reference_libraries_{fp_name}.csv', index_col= "Unnamed: 0")
        reference = reference_libraries.select_dtypes(exclude=['object']).as_matrix()
        numerical = np.concatenate((fp_matrix, reference), axis = 0)
        model = sklearn.decomposition.PCA(n_components=6, svd_solver = "full", whiten = True).fit(fp_matrix)
        pca_result = pd.DataFrame(model.transform(numerical), columns=['PC 1','PC 2',"PC 3", 'PC 4','PC 5',"PC 6"])
        ref_libraries = reference_libraries.select_dtypes(include=['object']).as_matrix()
        ref_final = np.concatenate((ref, ref_libraries), axis = 0)
        result = np.concatenate((pca_result, ref_final), axis = 1)
        result = pd.DataFrame(data=result, columns = ["PC 1", "PC 2", "PC 3", "PC 4", "PC 5", "PC 6", "Sequence", "Library"])
        #variance = list(model.explained_variance_ratio_)
        #self.a = round(variance[0] * 100, 2)
        #self.b = round(variance[1] * 100, 2)
        return result, model
