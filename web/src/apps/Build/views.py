import os, glob, csv, gc
import pandas as pd
from datetime import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from rest_framework.views import APIView

from .forms import InputForm
from modules.build.numerate import Numerate


class ServerViews(APIView):
    def post(self, request):
        form = InputForm(request.POST)
        form_dict = {
            "form": form,
        }
        if form.is_valid():
            form = form.save()
            now = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"database_{now}.csv"
            route = f"generated_csv/{filename}"

            numerate = Numerate(
                form.linear, form.methylated, form.topology, form.length
            )
            numerate.write_databases(path=route)

            request.session["csv_name"] = filename
            print("*" * 20)
            print(request.session)
            print("*" * 20)
            return redirect(f"/{filename}/")
        return render(request, "form_page.html", context=form_dict)

    def get(self, request):
        form = InputForm()
        form_dict = {
            "form": form,
        }
        return render(request, "form_page.html", context=form_dict)


class CSVView(APIView):
    def get(self, request, csv_name):
        data = pd.read_csv(f"generated_csv/{csv_name}", nrows=100)
        # data = pd.read_csv(f"{csv_name}", index_col="compound")
        # data = data.drop("Unnamed: 0", axis=1)
        data_html = data.to_html()
        context = {"loaded_data": data_html}

        # gc.collect()
        print("*" * 20)
        print(request.session)
        print("*" * 20)

        return render(request, "table.html", context)


class DownloadCSV(APIView):
    def get(self, request):
        csv_name = request.session["csv_name"]
        filename = f"generated_csv/{csv_name}"
        with open(filename, "rb") as csv_file:
            response = HttpResponse(csv_file, content_type="text/csv")
            response[
                "Content-Disposition"
            ] = f"attachment; filename = numerated_peptides.csv"
            return response


class ContactView(APIView):
    def get(self, request):
        return render(request, "contact.html")


class UserGuideView(APIView):
    def get(self, request):
        return render(request, "userguide.html")
