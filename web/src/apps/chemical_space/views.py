from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from rest_framework.views import APIView
from bokeh.embed import components

from apps.chemical_space.forms import ChemSpaceForm
from modules.chemical_space.pca import performPCA
from modules.chemical_space.tSNE import performTSNE
from modules.chemical_space.plot import Plot
from modules.fingerprint.compute_fingerprint import FP
from modules.fingerprint.AtomPair import BitCount


class ChemicalSpaceView(APIView):
    def post(self, request):
        form = ChemSpaceForm(request.POST)
        csv_name = request.session["csv_name"]
        if form.is_valid():
            form = form.save()
            if len(form.pca_fp) > 0:  # PCA FINGERPRINT
                fp_name = form.pca_fp
                feature_matrix, pep_id = BitCount(csv_name, fp_name).feature_matrix(
                    fp_name
                )
                result, a, b = performPCA().pca_fingerprint(
                    feature_matrix, pep_id, fp_name
                )
                plot = Plot(result).plot_pca(fp_name, a, b)
                script, div = components(plot)
                return render_to_response("plot.html", {"script": script, "div": div})
            else:
                pass
            if len(form.tsne_fp) > 0:
                fp_name = form.tsne_fp
                print(fp_name)
                feature_matrix, pep_id = BitCount(csv_name, fp_name).feature_matrix(
                    fp_name
                )
                result = performTSNE().tsne_fingerprint(feature_matrix, pep_id, fp_name)
                print(result.head())
                plot = Plot(result).plot_tsne(fp_name)
                script, div = components(plot)
                return render_to_response("plot.html", {"script": script, "div": div})
            if len(form.pca_pp) > 0:  # PCA DESCRIPTORS
                result, a, b = performPCA().pca_descriptors(csv_name)
                plot = Plot(result).plot_pca(["physicochemical properties"], a, b)
                script, div = components(plot)
                return render_to_response("plot.html", {"script": script, "div": div})
            else:
                pass
            if len(form.tsne_pp) > 0:  # TSNE DESCRIPTORS
                result = performTSNE().tsne_descriptors(csv_name)
                plot = Plot(result).plot_tsne(["physicochemical properties"])
                script, div = components(plot)
                return render_to_response("plot.html", {"script": script, "div": div})
            else:
                pass
        else:
            print("no idea")
        return render(request, "chemical_space.html", context={"form": form})

    def get(self, request):
        form = ChemSpaceForm()
        return render(request, "chemical_space.html", context={"form": form})
