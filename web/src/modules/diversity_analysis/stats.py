import pandas as pd 
import numpy as np

class Stat:
    def __init__(self):
        pass
    
    def statistical_values(self, result):
        libraries = result.Library.unique()
        min_ = np.array(result.groupby(['Library']).sim.min())
        mean = np.array(result.groupby(['Library']).sim.mean())
        median = np.array(result.groupby(['Library']).sim.median())
        std = np.array(result.groupby(['Library']).sim.std())
        var = np.array(result.groupby(['Library']).sim.var())
        max_ = np.array(result.groupby(['Library']).sim.max())
        data = np.concatenate((min_, mean, median, std, var, max_), axis = 0)
        data = np.reshape(data, (6, len(libraries)))
        data = np.around(data, decimals=3)
        stats = pd.DataFrame(data = data, columns = libraries , index = ["min", "mean", "median", "std", "var", "max"])
        return stats