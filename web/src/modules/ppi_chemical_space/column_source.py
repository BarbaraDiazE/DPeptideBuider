"""
column source, to allow bokeh plot
"""
import numpy as np
from bokeh.models import ColumnDataSource


def column_source(result, library: str):
    """
    input:
        result (DataFrame)
        library (str)
    Output:
        ColumnDataSource (bokeh object)
    """
    df = result[result["Library"] == library]
    x_axis = np.array(df["PC 1"])
    y_axis = np.array(df["PC 2"])
    n = np.array(df["chembl_id"])
    return ColumnDataSource(dict(x=x_axis, y=y_axis, N=n))
