"""PeptideBuilder URL Configuration

"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from apps.Build.views import (
    ServerViews,
    CSVView,
    DownloadCSV,
    ContactView,
    UserGuideView,
)
from apps.chemical_space.views import ChemicalSpaceView
from apps.diversity_analysis.views import DiversityAnalysisView
from apps.ppi_predictor.views import InputStructure, ServerHome
from apps.ppi_chemical_space.views import PPIChemicalSpaceView
urlpatterns = [
    url(r"^home/", ServerHome.as_view()),
    url(r"^input_structure/", InputStructure.as_view()),
    url(r"^peptides/csv/(?P<csv_name>.+)/$", CSVView.as_view()),
    url(r"^peptides/contact/", ContactView.as_view()),
    url(r"^peptides/chemspace/", ChemicalSpaceView.as_view()),
    url(r"^ppi/chemicalspace/", PPIChemicalSpaceView.as_view()),
    # url(r"^ppi/chemicalspace/plot/",SinglePPIChemicalSpaceView.as_view()),
    url(r"^peptides/diversity/", DiversityAnalysisView.as_view()),
    url(r"^peptides/", ServerViews.as_view()),
    url(r"^download_csv$", DownloadCSV.as_view()),
    url(r"^userguide/", UserGuideView.as_view()),
    path("admin/", admin.site.urls),
]
