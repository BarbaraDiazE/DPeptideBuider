import pandas as pd 
import numpy as np

def statistical_values(result, fp_name):
    """
    Output
    stats, html table that contains similarity statistical values for all libraries 
    """
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
    pep_stats = pd.DataFrame(data = data, columns = libraries , index = ["min", "mean", "median", "std", "var", "max"])
    ref_stats = pd.read_csv(f'modules/diversity_analysis/similarity_stats/stats_similarity_{fp_name}.csv', index_col = "Unnamed: 0")
    stats = pd.concat([pep_stats, ref_stats], axis = 1)
    stats = stats.to_html()
    return stats