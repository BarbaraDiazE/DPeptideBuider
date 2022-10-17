"""
column source, to allow bokeh plot
"""
import numpy as np
from bokeh.models import ColumnDataSource


def column_source(result, library):
    """
    input:
        result (DataFrame)
        Library (str)
    Output:
        ColumnDataSource (bokeh object)
    """

    df = result[result["Library"] == library]
    x_axis = np.array(df["sim"])
    y_axis = np.array(df["y"])

    return ColumnDataSource(dict(x=x_axis, y=y_axis))
