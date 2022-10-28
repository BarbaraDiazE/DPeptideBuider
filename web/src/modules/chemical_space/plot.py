# from bokeh.io import show, output_file
from bokeh.models import (
    # ColumnDataSource,
    LassoSelectTool,
    ZoomInTool,
    ZoomOutTool,
    SaveTool,
    HoverTool,
    PanTool,
    Legend,
)
from bokeh.plotting import figure
from bokeh.core.enums import LegendLocation
from modules.chemical_space.column_source import column_source

"""
Plot chemical space on DPeptideBuilder
"""


class Plot:
    def __init__(self):
        pass

    def plot_pca(self, result, a, b, algorith_name):
        fingerprint = "ECFP6"
        src1 = column_source(result, "FDA")
        src2 = column_source(result, "PPI")
        src3 = column_source(result, "MACRO")
        src4 = column_source(result, "NP")
        src5 = column_source(result, "FDA PEP")
        src6 = column_source(result, "linear")
        src7 = column_source(result, "cyclic")
        hover = HoverTool(
            tooltips=[
                ("PCA 1", "$x"),
                ("PCA 2", "$y"),
                ("NAME", "@N"),
            ]
        )
        p = figure(
            title=f"{algorith_name} based on {fingerprint}",
            x_axis_label="PC 1" + "(" + str(a) + "%)",
            y_axis_label="PC 2" + "(" + str(b) + "%)",
            x_range=(-4, 8),
            y_range=(-4, 8),
            tools=[hover],
            plot_width=1000,
            plot_height=800,
        )
        p.add_tools(
            LassoSelectTool(), ZoomInTool(), ZoomOutTool(), SaveTool(), PanTool()
        )
        FDA_plot = p.circle(x="x", y="y", source=src1, size=5, color="darkslateblue")
        PPI_plot = p.circle(x="x", y="y", source=src2, size=5, color="yellowgreen")
        MACRO_plot = p.circle(x="x", y="y", source=src3, size=5, color="lightsteelblue")
        NP_plot = p.circle(x="x", y="y", source=src4, size=5, color="olive")
        PEP_FDA_plot = p.circle(
            x="x",
            y="y",
            source=src5,
            size=5,
            color="lightcoral",
        )
        LIN_plot = p.circle(
            x="x",
            y="y",
            source=src6,
            size=5,
            color="teal",
        )
        CYC_plot = p.circle(x="x", y="y", source=src7, size=5, color="mediumvioletred")
        legend = Legend(
            items=[
                ("FDA", [FDA_plot]),
                ("PPI", [PPI_plot]),
                ("MACRO", [MACRO_plot]),
                ("NP", [NP_plot]),
                ("PEP FDA", [PEP_FDA_plot]),
                ("LIN", [LIN_plot]),
                ("CYC", [CYC_plot]),
            ],
            location="center",
            orientation="vertical",
            click_policy="hide",
        )
        p.add_layout(legend, place="right")
        p.xaxis.axis_label_text_font_size = "20pt"
        p.yaxis.axis_label_text_font_size = "20pt"
        p.xaxis.axis_label_text_color = "black"
        p.yaxis.axis_label_text_color = "black"
        p.xaxis.major_label_text_font_size = "18pt"
        p.yaxis.major_label_text_font_size = "18pt"
        p.title.text_font_size = "22pt"

        return p

    def plot_tsne(self, result, algorithm_name):
        fingerprint = "ECFP6"
        src1 = column_source(result, "FDA")
        src2 = column_source(result, "PPI")
        src3 = column_source(result, "MACRO")
        src4 = column_source(result, "NP")
        src5 = column_source(result, "FDA PEP")
        src6 = column_source(result, "linear")
        src7 = column_source(result, "cyclic")
        hover = HoverTool(
            tooltips=[
                ("PCA 1", "$x"),
                ("PCA 2", "$y"),
                ("NAME", "@N"),
            ]
        )
        p = figure(
            title=f"{algorithm_name} based on {fingerprint}",
            x_axis_label="PC 1",
            y_axis_label="PC 2",
            x_range=(-101, 101),
            y_range=(-101, 101),
            tools=[hover],
            plot_width=1000,
            plot_height=800,
        )
        p.add_tools(
            LassoSelectTool(), ZoomInTool(), ZoomOutTool(), SaveTool(), PanTool()
        )
        FDA_plot = p.circle(x="x", y="y", source=src1, size=5, color="darkslateblue")
        PPI_plot = p.circle(x="x", y="y", source=src2, size=5, color="yellowgreen")
        MACRO_plot = p.circle(
            x="x",
            y="y",
            source=src3,
            size=5,
            color="lightsteelblue",
        )
        NP_plot = p.circle(x="x", y="y", source=src4, size=5, color="olive")
        PEP_FDA_plot = p.circle(x="x", y="y", source=src5, size=5, color="lightcoral")
        LIN_plot = p.circle(x="x", y="y", source=src6, size=5, color="teal")
        CYC_plot = p.circle(x="x", y="y", source=src7, size=5, color="mediumvioletred")
        legend = Legend(
            items=[
                ("FDA", [FDA_plot]),
                ("PPI", [PPI_plot]),
                ("MACRO", [MACRO_plot]),
                ("NP", [NP_plot]),
                ("PEP FDA", [PEP_FDA_plot]),
                ("LIN", [LIN_plot]),
                ("CYC", [CYC_plot]),
            ],
            location="center",
            orientation="vertical",
            click_policy="hide",
        )
        p.add_layout(legend, place="right")
        p.xaxis.axis_label_text_font_size = "20pt"
        p.yaxis.axis_label_text_font_size = "20pt"
        p.xaxis.axis_label_text_color = "black"
        p.yaxis.axis_label_text_color = "black"
        p.xaxis.major_label_text_font_size = "18pt"
        p.yaxis.major_label_text_font_size = "18pt"
        p.title.text_font_size = "22pt"
        print("line 162", "## FUNCION PLOT ##")
        return p
