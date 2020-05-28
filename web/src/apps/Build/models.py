from django.db import models
from django import forms
from multiselectfield import MultiSelectField
from django.contrib.postgres.fields import HStoreField


class AminoAcid(models.Model):
    amino_acid = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.amino_acid


class DataAminoAcids(models.Model):
    name = models.ForeignKey(AminoAcid, on_delete=models.PROTECT, related_name="data")
    first_smile = models.CharField(max_length=264)
    first_abbreviation = models.CharField(max_length=5)
    linear_smile = models.CharField(max_length=264)
    linear_abbreviation = models.CharField(max_length=5)
    methylated_smile = models.CharField(max_length=264)
    methylated_abbreviation = models.CharField(max_length=5)

    def __str__(self):
        return self.name.amino_acid


class Oxygen(models.Model):
    oxygen_id = models.IntegerField(primary_key=True)
    linear = models.CharField(max_length=264)
    cyclic = models.CharField(max_length=264)


Keys = (
    ("ALA", "ALA (A)"),
    ("CYS", "CYS (C)"),
    ("ASP", "ASP (D)"),
    ("GLU", "GLU (E)"),
    ("PHE", "PHE (F)"),
    ("HIS", "HIS (H)"),
    ("ILE", "ILE (I)"),
    ("LYS", "LYS (K)"),
    ("LEU", "LEU (L)"),
    ("MET", "MET (M)"),
    ("ASN", "ASN (N)"),
    ("PRO", "PRO (P)"),
    ("GLN", "GLN (Q)"),
    ("ARG", "ARG (R)"),
    ("SER", "SER (S)"),
    ("THR", "THR (T)"),
    ("VAL", "VAL (V)"),
    ("TRP", "TRP (W)"),
    ("TYR", "TYR (Y)"),
    ("GLY", "GLY (G)"),
)
Met_keys = (
    ("ALA", "ALA (A)"),
    ("CYS", "CYS (C)"),
    ("ASP", "ASP (D)"),
    ("GLU", "GLU (E)"),
    ("PHE", "PHE (F)"),
    ("HIS", "HIS (H)"),
    ("ILE", "ILE (I)"),
    ("LYS", "LYS (K)"),
    ("LEU", "LEU (L)"),
    ("MET", "MET (M)"),
    ("ASN", "ASN (N)"),
    # ("PRO", "PRO (P)"),
    ("GLN", "GLN (Q)"),
    ("ARG", "ARG (R)"),
    ("SER", "SER (S)"),
    ("THR", "THR (T)"),
    ("VAL", "VAL (V)"),
    ("TRP", "TRP (W)"),
    ("TYR", "TYR (Y)"),
    ("GLY", "GLY (G)"),
)
topology = (("linear", "linear"), ("cyclic", "cyclic"))


class DataFormulary(models.Model):
    first = MultiSelectField(verbose_name="First position", choices=Keys, max_choices=1)
    linear = MultiSelectField(
        verbose_name="Linear", choices=Keys, max_choices=20, blank=True
    )
    methylated = MultiSelectField(
        verbose_name="Methylated", choices=Met_keys, max_choices=20, blank=True
    )
    topology = MultiSelectField(
        verbose_name="Topology", choices=topology, max_choices=2
    )
    length = models.IntegerField(verbose_name="Length", name="length")


# class NumeratedPep(models.Model):
#     """
#     session, now
#     data, dict, numerated
#     """

#     session = models.CharField(max_length=200)
#     data = HStoreField()

#     def __str__(self):
#         return self.session
