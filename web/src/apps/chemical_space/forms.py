from django import forms
from apps.chemical_space.models import Descriptors


class ChemSpaceForm(forms.ModelForm):
    class Meta:
        model = Descriptors
        fields = (
            "pca_fp",
            "tsne_fp",
            "pca_pp",
            "tsne_pp",
        )
