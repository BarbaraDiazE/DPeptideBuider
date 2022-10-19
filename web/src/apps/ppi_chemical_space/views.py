import os
from django.shortcuts import render, render_to_response, redirect
from rest_framework.views import APIView
from bokeh.embed import components

from apps.ppi_chemical_space.forms import PPIChemSpaceForm
from modules.ppi_chemical_space.pca import PcaFP
from modules.ppi_chemical_space.tSNE import performTSNE
from modules.ppi_chemical_space.plot import Plot
from modules.fingerprint.compute_fingerprint import FP
from modules.fingerprint.AtomPair import BitCount


class PPIChemicalSpaceView(APIView):

    def get(self, request):
        return render(request, "ppi_chemical_space.html")

# class SinglePPIChemicalSpaceView(APIView):
#     def get(self, request):
    def post(self, request):
        smiles = request.COOKIES.get("smiles")
        print("line 22")
        print(smiles)
        if smiles:
            print("tengo que calcular la descripcion")
            root_ = f"/src"
            input_file_ = "reference_database_ecfp6.csv"
            target = "library"
            id_columns = [
                "Library",
                "SMILES",
                "id",
                "chembl_id"
            ]
            result, a, b = PcaFP(root_, input_file_, target, id_columns).pca_fingerprint()
            print("line 28")
            print(result.head(2))
            fp_name = "ECFP6"
            print(result.head(2))
            plot = Plot(result).plot_pca(fp_name, a, b)
            script, div = components(plot)
            return  render_to_response("plot.html", {"script": script, "div": div})
        #     if len(form.tsne_fp) > 0:
        #         fp_name = form.tsne_fp
        #         print(fp_name)
        #         feature_matrix, pep_id = BitCount(csv_name, fp_name).feature_matrix(
        #             fp_name
        #         )
        #         result = performTSNE().tsne_fingerprint(feature_matrix, pep_id, fp_name)
        #         print(result.head())
        #         plot = Plot(result).plot_tsne(fp_name)
        #         script, div = components(plot)
        #         return render_to_response("plot.html", {"script": script, "div": div})
        #     if len(form.pca_pp) > 0:  # PCA DESCRIPTORS
        #         result, a, b = performPCA().pca_descriptors(csv_name)
        #         plot = Plot(result).plot_pca(["physicochemical properties"], a, b)
        #         script, div = components(plot)
        #         return render_to_response("plot.html", {"script": script, "div": div})
        #     else:
        #         pass
        #     if len(form.tsne_pp) > 0:  # TSNE DESCRIPTORS
        #         result = performTSNE().tsne_descriptors(csv_name)
        #         plot = Plot(result).plot_tsne(["physicochemical properties"])
        #         script, div = components(plot)
        #         return render_to_response("plot.html", {"script": script, "div": div})
        #     else:
        #         pass
        # else:
        #     print("no idea")
        return render(request, "ppi_chemical_space.html")

    def get(self, request):
        form = PPIChemSpaceForm()
        return render(request, "ppi_chemical_space.html")
