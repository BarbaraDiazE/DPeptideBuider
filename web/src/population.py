import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PeptideBuilder.settings')

import django
django.setup()

from apps.Build.models import AminoAcid, DataAminoAcids, Oxygen
from modules.build.amino_acid import dict_amino_acid
from modules.build.oxygen import dict_oxygen

data = dict_amino_acid
list_aminoacids = ["ALA", "CYS", "ASP", "GLU", "PHE", "HIS",  "ILE", "LYS", "LEU", "MET", "ASN", "PRO", "GLN", "ARG", "SER", "THR", "VAL", "TRP", "TYR", "GLY"]

def add_aminoacid(amino):
    A = AminoAcid.objects.get_or_create(amino_acid = amino)[0]
    A.save()
    return A

def populate_amino_acid(amino):
    a = DataAminoAcids(
                name = add_aminoacid(amino),
                first_smile = data[amino]["first_smile"],
                first_abbreviation = data[amino]["first_abbreviation"],
                linear_smile = data[amino]["linear_smile"],
                linear_abbreviation = data[amino]["linear_abbreviation"],
                methylated_smile = data[amino]["methylated_smile"],
                methylated_abbreviation = data[amino]["methylated_abbreviation"]
    )
    a.save()
    return a 

def populate_oxygen(length):
    b = Oxygen(
                oxygen_id = length,
                linear = dict_oxygen[length]["linear"],
                cyclic = dict_oxygen[length]["cyclic"],
    )
    b.save()
    return b

if __name__ == "__main__":
    for i in range(len(list_aminoacids)):
        populate_amino_acid(list_aminoacids[i])

list_length = [2,3,4,5,6]
if __name__ == "__main__":
    for i in list_length:
        populate_oxygen(i)
print("population is done")