from django import forms
from apps.chemical_space.models import Descriptors, FP_Keys, PP_Keys

class Chem_space_form(forms.ModelForm):
    class Meta:
        model = Descriptors
        fields = ( "pca_fp", "tsne_fp", "pca_pp", "tsne_pp",)

