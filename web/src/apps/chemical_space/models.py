from django.db import models
from multiselectfield import MultiSelectField

FP_Keys = (
    ("Atom Pairs", "Atom Pairs"),
    ("ECFP 6", "ECFP 6"),
)

PP_Keys = (("Physicochemical properties", "Physicochemical properties"),)


class Descriptors(models.Model):
    pca_fp = MultiSelectField(
        verbose_name="Fingerprint", choices=FP_Keys, max_choices=1, blank=True
    )
    tsne_fp = MultiSelectField(
        verbose_name="Fingerprint", choices=FP_Keys, max_choices=1, blank=True
    )
    pca_pp = MultiSelectField(
        verbose_name="Phisicochemical", choices=PP_Keys, max_choices=1, blank=True
    )
    tsne_pp = MultiSelectField(
        verbose_name="Phisicochemical", choices=PP_Keys, max_choices=1, blank=True
    )
