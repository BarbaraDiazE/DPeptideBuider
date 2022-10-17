from django import forms
from apps.chemical_space.models import Descriptors


class PPIPredictorForm(forms.ModelForm):
    class Meta:
        model = Descriptors
        fields = (
            "molecule",
        )
