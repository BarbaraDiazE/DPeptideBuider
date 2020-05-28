from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from rest_framework.views import APIView

import os, glob, csv

from bokeh.embed import components

from apps.chemical_space.forms import Chem_space_form

from modules.chemical_space.pca import performPCA
from modules.chemical_space.tSNE import performTSNE
from modules.chemical_space.plot import Plot
from modules.fingerprint.compute_fingerprint import FP
from modules.fingerprint.AtomPair import Bit_Count

# Create your views here.
class ChemicalSpaceView(APIView):
    def post(self, request):
        form = Chem_space_form(request.POST)
        csv_name = request.session["csv_name"]
        print("*" * 20)
        print(request.session)
        print("*" * 20)
        if form.is_valid():
            form = form.save()
            if len(form.pca_fp) > 0:  # PCA FINGERPRINT
                fp_name = form.pca_fp
                feature_matrix, pep_id = Bit_Count(csv_name, fp_name).feature_matrix(
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
            ######## TSNE update ###############3
            if len(form.tsne_fp) > 0:  # TSNE FINGERPRINT
                fp_name = form.tsne_fp
                print(fp_name)
                feature_matrix, pep_id = Bit_Count(csv_name, fp_name).feature_matrix(
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
        return render(request, "chemical_space.html", context={"form": form,})

    def get(self, request):
        form = Chem_space_form()
        return render(request, "chemical_space.html", context={"form": form,})
