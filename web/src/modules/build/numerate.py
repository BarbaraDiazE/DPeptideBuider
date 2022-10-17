import csv

from apps.Build.models import AminoAcid, DataAminoAcids, Oxygen

from .np_combinations import (
    combine_smiles,
    combine_linear_smiles,
    combine_cyclic_smiles,
    combine_abbr,
)
from modules.descriptors.descriptors import compute_descriptors


class Numerate:
    """
    Numerate peptides from amino acids
    """

    def __init__(self, linear, methylated, topology, length):
        self.linear = linear
        self.methylated = methylated
        self.topology = topology
        self.length = length

    def get_dataset(self):
        """
        return 
        dataset, list that contains amino acid SMILES (methyladed and linear from database)
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
        return dataset

    def get_abreviations(self):
        """
        return
        first_abbreviation and  abbr, letter representation for amino acids selected
        """
        linear_abbr_qs = AminoAcid.objects.filter(
            amino_acid__in=self.linear
        ).values_list("data__linear_abbreviation")
        methylated_abbr_qs = AminoAcid.objects.filter(
            amino_acid__in=self.methylated
        ).values_list("data__methylated_abbreviation")
        linear_abbr = list(map(lambda x: x[0], linear_abbr_qs))
        methylated_abbr = list(map(lambda x: x[0], methylated_abbr_qs))
        abbr = linear_abbr + methylated_abbr
        return abbr

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
        dataset = self.get_dataset()
        abbr = self.get_abreviations()
        linear, cyclic = self.get_oxygen()
        print("self.topology", self.topology)
        if len(self.topology) == 2:
            pep = combine_smiles(dataset, self.length)
            linear_peptides = combine_linear_smiles(pep, self.length, linear)
            linear_abbr = combine_abbr(abbr, self.length)
            linear_library = ["linear" for _ in linear_peptides]
            cyclic_peptides = combine_cyclic_smiles(pep, self.length, cyclic)
            cyclic_abbr = combine_abbr(abbr, self.length)
            cyclic_library = ["cyclic" for _ in cyclic_peptides]
            smiles = linear_peptides + cyclic_peptides
            ids = linear_abbr + cyclic_abbr
            libraries = linear_library + cyclic_library
        elif len(self.topology) == 1 and self.topology[0] == "linear":
            pep = combine_smiles(dataset, self.length)
            smiles = combine_linear_smiles(pep, self.length, linear)
            ids = combine_abbr(abbr, self.length)
            libraries = ["linear" for _ in smiles]
        elif len(self.topology) == 1 and self.topology[0] == "cyclic":
            pep = combine_smiles(dataset, self.length)
            smiles = combine_cyclic_smiles(pep, self.length, cyclic)
            ids = combine_abbr(abbr, self.length)
            libraries = ["cyclic" for _ in smiles]
        else:
            pass
        return smiles, ids, libraries

    def db_generator(self):
        smiles, ids, libraries = self.numerate()
        CanonicalSMILES, HBA, HBD, RB, LOGP, TPSA, MW = compute_descriptors(smiles)
        idx = (i + 1 for i in range(len(CanonicalSMILES)))
        for row in zip(
            idx, CanonicalSMILES, ids, libraries, HBA, HBD, RB, LOGP, TPSA, MW
        ):
            yield row

    def write_databases(self, path):
        """
        return 
        DF, Dataframe with numerated libraries, and physicochemical descriptors
        """
        header = [
            "compound",
            "SMILES",
            "Sequence",
            "Library",
            "HBA",
            "HBD",
            "RB",
            "LOGP",
            "TPSA",
            "MW",
        ]

        with open(path, "w") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(header)
            writer.writerows(self.db_generator())
