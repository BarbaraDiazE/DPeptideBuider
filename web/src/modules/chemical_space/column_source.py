"""
column source, to allow bokeh plot
"""
import bokeh
from bokeh.models import ColumnDataSource

def column_source(result, Library):
    X = list()
    Y = list()
    N = list()
    DF = result[result["Library"] == Library]
    X = list(DF["PC 1"])
    Y = list(DF["PC 2"])
    N = list(DF["Sequence"])
        
    return ColumnDataSource(dict(x = X, y = Y, N = N))
