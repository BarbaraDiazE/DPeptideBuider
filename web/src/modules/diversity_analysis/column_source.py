"""
column source, to allow bokeh plot
"""
import numpy as np
import bokeh
from bokeh.models import ColumnDataSource

def column_source(result, Library):
    """
    input:
        result (DataFrame)
        Library (str)
    Output:
        ColumnDataSource (bokeh object)
    """

    DF = result[result["Library"] == Library]
    X = np.array(DF["sim"])
    Y = np.array(DF["y"])
        
    return ColumnDataSource(dict(x = X, y = Y))
