import os
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA as PCAalgorithm
import joblib


def loadings(model, numerical_descriptors):
    # loadings =
    loadings = np.transpose(model.components_)
    pca_loadings = pd.DataFrame(
        data=loadings, index=numerical_descriptors, columns=["PC 1", "PC 2", "PC 3"],
    )
    print("loadings", "\n", pca_loadings.head())
    return pca_loadings


class PcaFP:
    def __init__(self, root, input_file, target, id_columns):
        self.data = pd.read_csv(f"{root}/modules/{input_file}", low_memory=False)
        self.id_columns = id_columns
        print(self.data.head())
        print("Libraries are: ", self.data.library.unique())
        print("Total compounds: ", self.data.shape[0])
        self.target = target
        self.root = root

    def get_numerical_data(self):
        descriptors = self.data.columns.to_list()
        for i in self.id_columns:
            descriptors.remove(i)
        numerical_data = self.data[descriptors]
        return numerical_data

    def get_id_data(self):
        return self.data[self.id_columns]

    def save(
            self,
            model,
            output_reference: str
        ):
        trained_model_root = f"{self.root}/trained_models"
        output_model_name = f"{output_reference}.pkl"
        joblib.dump(model, os.path.join(trained_model_root, output_model_name))
        print(f"saved model")

    def pca_fingerprint(self):
        """
        output
            result: Data Frame with PCA result,
            a, variance PC 1
            b, variance PC 2
        """
        numerical_data = self.get_numerical_data()
        model = PCAalgorithm(
            n_components=6,
            svd_solver="full",
            whiten=True
        ).fit(numerical_data)
        # self.save(model, "pca_model")
        pca_result = pd.DataFrame(
            data = model.transform(numerical_data),
            columns = [
                "PC 1",
                "PC 2",
                "PC 3",
                "PC 4",
                "PC 5",
                "PC 6",
            ],
            # columns=self.descriptors,
        )
        print(pca_result.head(2))
        id_data = self.get_id_data()
        print(id_data.head(2))
        result = pd.concat([id_data, pca_result], axis=1)
        a = round(list(model.explained_variance_ratio_)[0] * 100, 2)
        b = round(list(model.explained_variance_ratio_)[1] * 100, 2)
        print("line 83")
        print("si me ejecuto")
        return result, a, b
