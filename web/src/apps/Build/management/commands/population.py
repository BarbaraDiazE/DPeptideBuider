import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PeptideBuilder.settings")

from django.core.management.base import BaseCommand
from django.conf import settings

from apps.Build.models import AminoAcid, DataAminoAcids, Oxygen
from modules.build.amino_acid import dict_amino_acid
from modules.build.oxygen import dict_oxygen


class Command(BaseCommand):
    help = "Populate database"

    def add_aminoacid(self, amino):
        A = AminoAcid.objects.get_or_create(amino_acid=amino)[0]
        A.save()
        return A

    def populate_amino_acid(self, amino):
        data = dict_amino_acid
        a = DataAminoAcids(
            name=self.add_aminoacid(amino),
            first_smile=data[amino]["first_smile"],
            first_abbreviation=data[amino]["first_abbreviation"],
            linear_smile=data[amino]["linear_smile"],
            linear_abbreviation=data[amino]["linear_abbreviation"],
            methylated_smile=data[amino]["methylated_smile"],
            methylated_abbreviation=data[amino]["methylated_abbreviation"],
        )
        a.save()
        return a

    def populate_oxygen(self, length):
        b = Oxygen(
            oxygen_id=length,
            linear=dict_oxygen[length]["linear"],
            cyclic=dict_oxygen[length]["cyclic"],
        )
        b.save()
        return b

    def handle(self, *arg, **kwargs):
        list_aminoacids = [
            "ALA",
            "CYS",
            "ASP",
            "GLU",
            "PHE",
            "HIS",
            "ILE",
            "LYS",
            "LEU",
            "MET",
            "ASN",
            "PRO",
            "GLN",
            "ARG",
            "SER",
            "THR",
            "VAL",
            "TRP",
            "TYR",
            "GLY",
        ]
        DataAminoAcids.objects.all().delete()
        AminoAcid.objects.all().delete()
        Oxygen.objects.all().delete()
        for i in range(len(list_aminoacids)):
            self.populate_amino_acid(list_aminoacids[i])
            continue
        list_length = [2, 3, 4, 5, 6]
        for i in list_length:
            self.populate_oxygen(i)
            continue
        self.stdout.write("Table populated")
