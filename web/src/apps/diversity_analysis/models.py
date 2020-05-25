from django.db import models
from multiselectfield import MultiSelectField

FP_Keys = (("Atom Pair", "Atom Pair"),)


class SelectFingerprint(models.Model):
    fp = MultiSelectField(
        verbose_name="Fingerprint", choices=FP_Keys, max_choices=1, blank=True
    )
