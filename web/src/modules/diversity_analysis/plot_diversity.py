import pandas as pd
import numpy as np

from bokeh.io import  show, output_file
from bokeh.models import ColumnDataSource, LassoSelectTool, ZoomInTool, ZoomOutTool, SaveTool, HoverTool,PanTool, Legend
from bokeh.plotting import figure
from bokeh.core.enums import LegendLocation

"""
Plot diversity anslysis result
"""

from bokeh.io import  show, output_file
from bokeh.models import ColumnDataSource, LassoSelectTool, ZoomInTool, ZoomOutTool, SaveTool, HoverTool, PanTool, Legend
from bokeh.plotting import figure
from bokeh.core.enums import LegendLocation
import os
from modules.diversity_analysis.column_source import column_source

class Plot:
    
    def __init__(self, result):
        self.result = result
    
    def plot_similarity(self, parameter):
        result = self.result
        source1 = column_source(result, "FDA")
        source2 = column_source(result, "PPI")
        source3 = column_source(result, "MACRO")
        source4 = column_source(result, "NP")
        source5 = column_source(result, "FDA PEP")
        source6 = column_source(result, "linear")
        source7 = column_source(result, "cyclic")
        hover = HoverTool(tooltips = [
                                        ("sim","$x"),
                                        ("CDF","$y"),
                                        ])
        p = figure(title = "CDF of Tanimoto Similarity, based on: " + parameter[0],
                x_axis_label = "Similarity", y_axis_label="Cumulative Distribution Function",
                x_range = (0,1), y_range = (0,1), tools=[hover], plot_width = 1000, plot_height = 800)
        p.add_tools(LassoSelectTool(), ZoomInTool(), ZoomOutTool(), SaveTool(), PanTool())
        FDA_plot = p.line(x = "x", y = "y", source = source1, color = "darkslateblue", line_width = 3)
        PPI_plot = p.line(x = "x", y = "y", source = source2, color = "yellowgreen", line_width = 3)
        MACRO_plot = p.line(x = "x", y = "y", source = source3, color ="lightsteelblue", line_width = 3)
        NP_plot = p.line(x = "x", y = "y", source = source4, color = "olive", line_width = 3)
        PEP_FDA_plot = p.line(x = "x", y = "y", source = source5, color ="darkslategray", line_width = 3)
        LIN_plot = p.line(x = "x", y = "y", source = source6, color = "teal", line_width = 3)
        CYC_plot = p.line(x = "x", y = "y", source = source7, color = "mediumvioletred", line_width = 3)
        legend = Legend(items=[
                    ("FDA",     [FDA_plot]),
                    ("PPI",     [PPI_plot]),
                    ("MACRO",   [MACRO_plot]),
                    ("NP",      [NP_plot]),
                    ("PEP FDA", [PEP_FDA_plot]),
                    ("LIN",     [LIN_plot]),
                    ("CYC",     [CYC_plot]),
                ], 
                location = "center", orientation = "vertical", click_policy = "hide"
            )
        p.add_layout(legend, place = 'right')
        p.xaxis.axis_label_text_font_size = "20pt"
        p.yaxis.axis_label_text_font_size = "20pt"
        p.xaxis.axis_label_text_color = "black"
        p.yaxis.axis_label_text_color = "black"
        p.xaxis.major_label_text_font_size = "18pt"
        p.yaxis.major_label_text_font_size = "18pt"
        p.title.text_font_size = "22pt"
        
        return p
