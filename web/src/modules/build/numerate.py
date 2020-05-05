import pandas as pd

from apps.Build.models import AminoAcid, DataAminoAcids, Oxygen
from .combinations import (
    # combine_linear_smiles,
    combine_cyclic_smiles,
    # ,
    # combine_abbr,
)
from .np_combinations import (
    combine_smiles,
    combine_linear_smiles,
    combine_abbr,
)
from modules.descriptors.descriptors import compute_descriptors


class Numerate:
    """
    Numerate peptides from amino acids
    """

    def __init__(self, first, linear, methylated, topology, length):
        self.first = first
        self.linear = linear
        self.methylated = methylated
        self.topology = topology
        self.length = length

    def get_first(self):
        """
        return, first(smiles from database)
        """
        _ = AminoAcid.objects.filter(amino_acid=self.first)[0]
        first = DataAminoAcids.objects.filter(name=_).all()[0].first_smile
        return first

    def get_dataset(self):
        """
        return 
        dataset, list that contains amino acid smiles (methyladed and linear from database)
        """
        linear_qs = AminoAcid.objects.filter(amino_acid__in=self.linear).values_list(
            "data__linear_smile"
        )
        print("linear_qs", linear_qs)
        methylated_qs = AminoAcid.objects.filter(
            amino_acid__in=self.methylated
        ).values_list("data__methylated_smile")
        linear_dataset = list(map(lambda x: x[0], linear_qs))
        methylated_dataset = list(map(lambda x: x[0], methylated_qs))
        dataset = linear_dataset + methylated_dataset
        print("dataset", dataset)
        return dataset

    def get_abreviations(self):
        """
        return
        first_abbreviation and  abbr, letter representation for amino acids selected
        """
        _ = AminoAcid.objects.filter(amino_acid=self.first)[0]
        first_abbreviation = (
            DataAminoAcids.objects.filter(name=_).all()[0].first_abbreviation
        )
        linear_abbr_qs = AminoAcid.objects.filter(
            amino_acid__in=self.linear
        ).values_list("data__linear_abbreviation")
        methylated_abbr_qs = AminoAcid.objects.filter(
            amino_acid__in=self.methylated
        ).values_list("data__methylated_abbreviation")
        linear_abbr = list(map(lambda x: x[0], linear_abbr_qs))
        methylated_abbr = list(map(lambda x: x[0], methylated_abbr_qs))
        abbr = linear_abbr + methylated_abbr
        return first_abbreviation, abbr

    def get_oxygen(self):
        """
        return
        linear, cyclic are oxygen smiles accord to peptide length and libraries' topology
        """
        linear = str()
        linear = Oxygen.objects.filter(oxygen_id=self.length)[0].linear
        cyclic = str()
        cyclic = Oxygen.objects.filter(oxygen_id=self.length)[0].cyclic
        return linear, cyclic

    def numerate(self):
        """
        return
        smiles, Canonical smiles of generated libraries
        ids, sequence peptide representation
        libraries, list with libraries' name
        """
        first = self.get_first()
        dataset = self.get_dataset()
        first_abbreviation, abbr = self.get_abreviations()
        linear, cyclic = self.get_oxygen()
        if len(self.topology) == 2:
            pep = combine_smiles(first, dataset, self.length, linear)
            linear_peptides = combine_linear_smiles(pep, self.length, linear)
            print("linear peptides")
            print(len(linear_peptides))
            linear_abbr = combine_abbr(first_abbreviation, abbr, self.length)
            linear_library = ["linear" for _ in linear_peptides]
            cyclic_peptides = combine_cyclic_smiles(first, dataset, self.length, cyclic)
            cyclic_abbr = combine_abbr(first_abbreviation, abbr, self.length)
            print("cyclic peptides")
            print(len(cyclic_peptides))
            cyclic_library = ["cyclic" for _ in cyclic_peptides]
            smiles = linear_peptides + cyclic_peptides
            print(smiles[:5])
            print("linear abreviation", linear_abbr[:5])
            print("cyclic abreviation", cyclic_abbr[:5])
            ids = linear_abbr + cyclic_abbr
            print(ids[:5])
            libraries = linear_library + cyclic_library
        elif len(self.topology) == 0 and self.topology[0] == "linear":
            # smiles = combine_linear_smiles(first, dataset, self.length, linear)
            pep = combine_smiles(first, dataset, self.length, linear)
            smiles = combine_linear_smiles(pep, self.length, linear)
            ids = combine_abbr(first_abbreviation, abbr, self.length)
            libraries = ["linear" for _ in linear_peptides]
        elif len(self.topology) == 0 and self.topology[0] == "cyclic":
            smiles = combine_cyclic_smiles(first, dataset, self.length, cyclic)
            ids = combine_abbr(first_abbreviation, abbr, self.length)
            libraries = ["cyclic" for _ in cyclic_peptides]
        else:
            pass
        return smiles, ids, libraries

    def write_databases(self):
        """
        return 
        DF, Dataframe with numerated libraries, and physicochemical descriptors
        """
        smiles, ids, libraries = self.numerate()
        CanonicalSMILES, HBA, HBD, RB, LOGP, TPSA, MW = compute_descriptors(smiles)
        data = {
            "SMILES": CanonicalSMILES,
            "Sequence": ids,
            "Library": libraries,
            "HBA": HBA,
            "HBD": HBD,
            "RB": RB,
            "LOGP": LOGP,
            "TPSA": TPSA,
            "MW": MW,
        }
        DF = pd.DataFrame.from_dict(data)
        return DF
