from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext

import os, glob, csv
import pandas as pd

from bokeh.embed import components

from rest_framework.views import APIView
from apps.diversity_analysis.forms import Diversity_Analysis_Form

from modules.fingerprint.compute_fingerprint import FP
from modules.diversity_analysis.plot_diversity import Plot
from modules.diversity_analysis.stats import Stat

class DiversityAnalysisView(APIView):
    
    def post(self, request):
        form = Diversity_Analysis_Form(request.POST)
        csv_name = request.session['csv_name']  
        form_dict = {'form' : form, }
        if form.is_valid():
            form = form.save()
            fp_name = form.fp
            result = FP(csv_name, fp_name).similarity(fp_name)
            print(result.head())
            print(result.Library.unique())
            print(result.shape[0])
            plot = Plot(result).plot_similarity(fp_name)
            script, div = components(plot)
            stats = Stat().statistical_values(result)
            stats = stats.to_html()
            return render_to_response('plot_diversity.html', {'script': script, 'div': div, "stats":stats})
        return render(request,'diversity_analysis.html', context = form_dict)

    def get(self, request):
        form = Diversity_Analysis_Form(request.POST)
        form_dict = {'form' : form, }
        return render(request,'diversity_analysis.html', context = form_dict)