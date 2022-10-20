"""
Plot IPP molecule vs reference libraries chemical space
"""
from bokeh.models import (
    ColumnDataSource,
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
from modules.ppi_chemical_space.column_source import column_source


class PPIPlot:
    def __init__(self, result):
        self.result = result

    def plot_pca(self, parameter: list, a, b, algorithm_name: str):
        result = self.result
        src1 = column_source(result, "FDA")
        src2 = column_source(result, "PPI")
        src3 = column_source(result, "MACRO")
        src4 = column_source(result, "NP")
        src5 = column_source(result, "FDA PEP")
        src6 = column_source(result, "Test Compound")
        hover = HoverTool(
            tooltips=[
                ("PCA 1", "$x"),
                ("PCA 2", "$y"),
                ("NAME", "@N"),
            ]
        )
        p = figure(
            title=f"{algorithm_name} based on {parameter[0]}",
            x_axis_label=f"PC 1 ({str(a)} %)",
            y_axis_label=f"PC 2 ({str(b)} %)",
            x_range=(-4, 8),
            y_range=(-4, 8),
            tools=[hover],
            plot_width=1000,
            plot_height=800,
        )
        p.add_tools(
            LassoSelectTool(), ZoomInTool(), ZoomOutTool(), SaveTool(), PanTool()
        )
        fda_plot = p.circle(
            x="x",
            y="y",
            size=5,
            source=src1,
            color="darkslateblue",
        )
        ppi_plot = p.circle(x="x", y="y", size=5, source=src2, color="yellowgreen")
        macro_plot = p.circle(x="x", y="y", size=5, source=src3, color="lightsteelblue")
        np_plot = p.circle(x="x", y="y", source=src4, size=5, color="olive")
        pep_fda_plot = p.circle(x="x", y="y", source=src5, size=5, color="lightcoral")
        ppi_molecule_plot = p.circle(x="x", y="y", size=5, source=src6, color="red")
        legend = Legend(
            items=[
                ("FDA", [fda_plot]),
                ("PPI", [ppi_plot]),
                ("MACRO", [macro_plot]),
                ("NP", [np_plot]),
                ("PEP FDA", [pep_fda_plot]),
                ("Test molecule", [ppi_molecule_plot]),
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

    def plot_tsne(self, parameter, algorithm_name: str):
        result = self.result
        src1 = column_source(result, "FDA")
        src2 = column_source(result, "PPI")
        src3 = column_source(result, "MACRO")
        src4 = column_source(result, "NP")
        src5 = column_source(result, "FDA PEP")
        src6 = column_source(result, "Test Compound")
        hover = HoverTool(
            tooltips=[
                ("PCA 1", "$x"),
                ("PCA 2", "$y"),
                ("NAME", "@N"),
            ]
        )
        p = figure(
            title=f"{algorithm_name} based on {parameter[0]}",
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
        fda_plot = p.circle(
            x="x",
            y="y",
            size=5,
            source=src1,
            color="darkslateblue",
        )
        ppi_plot = p.circle(x="x", y="y", size=5, source=src2, color="yellowgreen")
        macro_plot = p.circle(x="x", y="y", size=5, source=src3, color="lightsteelblue")
        np_plot = p.circle(x="x", y="y", source=src4, size=5, color="olive")
        pep_fda_plot = p.circle(x="x", y="y", source=src5, size=5, color="lightcoral")
        ppi_molecule_plot = p.circle(x="x", y="y", size=5, source=src6, color="red")
        legend = Legend(
            items=[
                ("FDA", [fda_plot]),
                ("PPI", [ppi_plot]),
                ("MACRO", [macro_plot]),
                ("NP", [np_plot]),
                ("PEP FDA", [pep_fda_plot]),
                ("Test molecule", [ppi_molecule_plot]),
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
