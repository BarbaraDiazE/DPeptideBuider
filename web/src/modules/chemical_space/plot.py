from bokeh.io import  show, output_file
from bokeh.models import ColumnDataSource, LassoSelectTool, ZoomInTool, ZoomOutTool, SaveTool, HoverTool, PanTool, Legend
from bokeh.plotting import figure
from bokeh.core.enums import LegendLocation
import os
from modules.chemical_space.column_source import column_source
"""
Plot chemical space
"""
class Plot:
    def __init__(self, result):
        self.result = result
    
    def plot_pca(self, parameter):
        result = self.result
        source1 = column_source(result, "FDA")
        source2 = column_source(result, "PPI")
        source3 = column_source(result, "MACRO")
        source4 = column_source(result, "NP")
        source5 = column_source(result, "FDA PEP")
        source6 = column_source(result, "linear")
        source7 = column_source(result, "cyclic")
        hover = HoverTool(tooltips = [
                                        ("PCA 1","$x"),
                                        ("PCA 2","$y"),
                                        ("NAME","@N"),
                                        ])
        p = figure(title = "PCA based on: " + parameter[0],
                x_axis_label = "PC 1", y_axis_label="PC 2",
                x_range = (-7,7), y_range = (-7,7), tools = [hover], plot_width = 1000, plot_height = 800)
        p.add_tools(LassoSelectTool(), ZoomInTool(), ZoomOutTool(), SaveTool(), PanTool())
        p.add_tools(SaveTool())
        FDA_plot = p.circle(x = "x", y = "y", source = source1, color = "darkslateblue", size = 5)
        PPI_plot = p.circle(x = "x", y = "y", source = source2, color = "yellowgreen", size = 5)
        MACRO_plot = p.circle(x = "x", y = "y", source = source3, color ="lightsteelblue", size = 5)
        NP_plot = p.circle(x = "x", y = "y", source = source4, color = "olive", size = 5)
        PEP_FDA_plot = p.circle(x = "x", y = "y", source = source5, color ="lightcoral", size = 5)
        LIN_plot = p.circle(x = "x", y = "y", source = source6, color = "teal", size = 5)
        CYC_plot = p.circle(x = "x", y = "y", source = source7, color = "mediumvioletred", size = 5)
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

    def plot_tsne(self, parameter):
        result = self.result
        source1 = column_source(result, "FDA")
        source2 = column_source(result, "PPI")
        source3 = column_source(result, "MACRO")
        source4 = column_source(result, "NP")
        source5 = column_source(result, "FDA PEP")
        source6 = column_source(result, "linear")
        source7 = column_source(result, "cyclic")
        hover = HoverTool(tooltips = [
                                        ("PCA 1","$x"),
                                        ("PCA 2","$y"),
                                        ("NAME","@N"),
                                        ])
        p = figure(title = "tSNE based on " + parameter[0],
                x_axis_label = "PC 1", y_axis_label="PC 2",
                x_range = (-7,7), y_range = (-7,7), tools = [hover], plot_width = 1000, plot_height = 800)
        p.add_tools(LassoSelectTool(), ZoomInTool(), ZoomOutTool(), SaveTool(), PanTool())
        p.add_tools(SaveTool())
        FDA_plot = p.circle(x = "x", y = "y", source = source1, color = "darkslateblue", size = 5)
        PPI_plot = p.circle(x = "x", y = "y", source = source2, color = "yellowgreen", size = 5)
        MACRO_plot = p.circle(x = "x", y = "y", source = source3, color ="lightsteelblue", size = 5)
        NP_plot = p.circle(x = "x", y = "y", source = source4, color = "olive", size = 5)
        PEP_FDA_plot = p.circle(x = "x", y = "y", source = source5, color ="lightcoral", size = 5)
        LIN_plot = p.circle(x = "x", y = "y", source = source6, color = "teal", size = 5)
        CYC_plot = p.circle(x = "x", y = "y", source = source7, color = "mediumvioletred", size = 5)
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
