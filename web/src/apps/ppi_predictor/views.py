from django.shortcuts import render, render_to_response, redirect
from rest_framework.views import APIView
from django.http import JsonResponse
from modules.ppi_predictor.ppi_predictor import molecule_prediction


class ServerHome(APIView):
    def get(self, request):
        return render(request, "home.html")


class InputStructure(APIView):
    def get(self, request):
        smiles = request.GET.get('smiles')
        if smiles:
            data = molecule_prediction(smiles)
            print(data)
            return JsonResponse(
                {
                    "smiles": smiles,
                    "resultTable": data.to_html(justify="center"),
                }
            )
    # except Exception as e:
    #     return str(e)
