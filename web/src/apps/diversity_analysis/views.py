from django.shortcuts import render, render_to_response
from django.template import RequestContext

import os, glob, csv

from bokeh.embed import components

from rest_framework.views import APIView

from apps.diversity_analysis.forms import Diversity_Analysis_Form

from modules.fingerprint.compute_fingerprint import FP
from modules.diversity_analysis.plot_diversity import Plot


class DiversityAnalysisView(APIView):
    def post(self, request):
        form = Diversity_Analysis_Form(request.POST)
        csv_name = request.session["csv_name"]
        if form.is_valid():
            form = form.save()
            fp_name = form.fp
            result, stats = FP(csv_name, fp_name).similarity(fp_name)
            plot = Plot().plot_similarity(result, fp_name)
            script, div = components(plot)
            return render_to_response(
                "plot_diversity.html", {"script": script, "div": div, "stats": stats}
            )
        return render(request, "diversity_analysis.html", context={"form": form,})

    def get(self, request):
        form = Diversity_Analysis_Form(request.POST)
        return render(request, "diversity_analysis.html", context={"form": form,})
