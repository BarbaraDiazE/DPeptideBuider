import os
from django.shortcuts import render, render_to_response, redirect
from rest_framework.views import APIView
from bokeh.embed import components

from apps.ppi_chemical_space.forms import PPIChemSpaceForm
from modules.ppi_chemical_space.pca import PcaFP
from modules.ppi_chemical_space.tSNE import TsneFP
from modules.ppi_chemical_space.ipp_plot import PPIPlot
from modules.fingerprint.compute_fingerprint import FP


class PPIChemicalSpaceView(APIView):
    def get(self, request):
        return render(request, "ppi_chemical_space.html")

    def post(self, request):
        cookie_value = request.COOKIES.get("myCookie")
        values = cookie_value.split("&")
        test_smiles = values[0].split("=")[1].replace("'", "")
        algorithm = values[1].split("=")[1].replace("'", "")
        if test_smiles:
            root_ = f"/src"
            input_file_ = "reference_database_ecfp6.csv"
            target = "library"
            fp_name = [
                "ECFP6",
            ]
            try:
                if algorithm == "Visualize PCA":
                    id_columns = ["Library", "SMILES", "chembl_id"]
                    pca = PcaFP(root_, input_file_, target, id_columns, test_smiles)
                    result, a, b, a_name = pca.pca_fingerprint()
                    plot = PPIPlot(result).plot_pca(fp_name, a, b, a_name)
                    script, div = components(plot)
                    return render_to_response(
                        "plot.html", {"script": script, "div": div}
                    )
                if algorithm == "Visualize t-SNE":
                    id_columns = [
                        "Library",
                        "SMILES",
                        "chembl_id",
                    ]
                    tsne = TsneFP(root_, input_file_, target, id_columns, test_smiles)
                    result, a_name = tsne.tsne_fingerprint()
                    plot = PPIPlot(result).plot_tsne(fp_name, a_name)
                    script, div = components(plot)
                    return render_to_response(
                        "plot.html", {"script": script, "div": div}
                    )
            except Exception as e:
                print(e)
        return render(request, "ppi_chemical_space.html")

    def get(self, request):
        form = PPIChemSpaceForm()
        return render(request, "ppi_chemical_space.html")
