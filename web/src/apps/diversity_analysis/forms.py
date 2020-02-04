from django import forms
from apps.diversity_analysis.models import SelectFingerprint

class Diversity_Analysis_Form(forms.ModelForm):
    class Meta:
        model = SelectFingerprint
        fields = ( "fp", )