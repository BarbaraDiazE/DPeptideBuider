from django import forms
from apps.Build.models import  DataFormulary

    
class InputForm(forms.ModelForm):
    class Meta:
        model = DataFormulary
        fields = ( "first", "linear", "methylated", "topology", "length")