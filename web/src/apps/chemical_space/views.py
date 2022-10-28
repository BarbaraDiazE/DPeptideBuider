from calendar import c
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from rest_framework.views import APIView
from bokeh.embed import components

from apps.chemical_space.forms import ChemSpaceForm
from modules.chemical_space.pca import performPCA
from modules.chemical_space.tSNE import performTSNE
from modules.chemical_space.plot import Plot


class ChemicalSpaceView(APIView):
    def post(self, request):
        form = ChemSpaceForm(request.POST)
        csv_name = request.session["csv_name"]
        root_ = f"/src"
        if form.is_valid():
            form = form.save()
            ### PCA FP ###
            if len(form.pca_fp) > 0:
                fp_name = form.pca_fp
                result, a, b, al_name = performPCA().pca_fingerprint(root_, csv_name)
                plot = Plot().plot_pca(result, a, b, al_name)
                script, div = components(plot)
                return render_to_response("plot.html", {"script": script, "div": div})
            else:
                pass
            ### TSNE FP ###
            if len(form.tsne_fp) > 0:
                fp_name = form.tsne_fp
                result, al_name = performTSNE().tsne_fingerprint(root_, csv_name)
                plot = Plot().plot_tsne(result, al_name)
                script, div = components(plot)
                return render_to_response(
                    "plot_dpeptides.html", {"script": script, "div": div}
                )
            ### PCA DESCRIPTORS ###
            if len(form.pca_pp) > 0:
                result, a, b, al_name = performPCA().pca_descriptors(root_, csv_name)
                plot = Plot().plot_pca(result, a, b, al_name)
                script, div = components(plot)
                return render_to_response(
                    "plot_dpeptides.html", {"script": script, "div": div}
                )
            else:
                pass
            ### TSNE DESCRIPTORS ###
            if len(form.tsne_pp) > 0:  # TSNE DESCRIPTORS
                result, al_name = performTSNE().tsne_descriptors(root_, csv_name)
                plot = Plot().plot_tsne(result, al_name)
                script, div = components(plot)
                return render_to_response(
                    "plot_dpeptides.html", {"script": script, "div": div}
                )
            else:
                pass
        else:
            print("no idea")
        return render(request, "chemical_space.html", context={"form": form})

    def get(self, request):
        form = ChemSpaceForm()
        return render(request, "chemical_space.html", context={"form": form})
