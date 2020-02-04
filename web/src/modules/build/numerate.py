
import pandas as pd

from apps.Build.models import AminoAcid, DataAminoAcids, Oxygen
from .combinations import combine_linear_smiles, combine_cyclic_smiles, combine_abbreviations
from modules.descriptors.descriptors import compute_descriptors

class Numerate:
    """
    Numerate peptides from amino acids
    """

    def __init__(self, first , linear, methylated, topology, length):
        self.first = first
        self.linear = linear
        self.methylated = methylated
        self.topology = topology
        self.length = length
        
    def get_first(self):
        """
        return, first(smiles from database)
        """
        _ = AminoAcid.objects.filter(amino_acid = self.first)[0]
        first = DataAminoAcids.objects.filter(name = _).all()[0].first_smile
        return first

    def get_dataset(self):
        """
        return 
        dataset, list that contains amino acid smiles (methyladed and linear from database)
        """
        linear_qs = AminoAcid.objects.filter(amino_acid__in=self.linear)\
            .values_list('data__linear_smile')
        methylated_qs = AminoAcid.objects.filter(amino_acid__in=self.methylated)\
            .values_list('data__methylated_smile')
        linear_dataset = list(map(lambda x: x[0], linear_qs))
        methylated_dataset = list(map(lambda x: x[0], methylated_qs))
        dataset = linear_dataset + methylated_dataset
        return dataset
    
    def get_abreviations(self):
        """
        return
        first_abbreviation and  abbreviations, letter representation for amino acids selected
        """
        _ = AminoAcid.objects.filter(amino_acid = self.first)[0]
        first_abbreviation = DataAminoAcids.objects.filter(name = _).all()[0].first_abbreviation
        linear_abbreviations_qs = AminoAcid.objects.filter(amino_acid__in=self.linear)\
            .values_list('data__linear_abbreviation')
        methylated_abbreviations_qs = AminoAcid.objects.filter(amino_acid__in=self.methylated)\
            .values_list('data__methylated_abbreviation')
        linear_abbreviations = list(map(lambda x: x[0], linear_abbreviations_qs))
        methylated_abbreviations = list(map(lambda x: x[0], methylated_abbreviations_qs))
        abbreviations = linear_abbreviations + methylated_abbreviations
        return first_abbreviation, abbreviations
        
        
    def get_oxygen(self):
        """
        return
        linear, cyclic are oxygen smiles accord to peptide length and libraries' topology
        """
        linear = str()
        linear = Oxygen.objects.filter(oxygen_id = self.length)[0].linear
        cyclic = str()
        cyclic = Oxygen.objects.filter(oxygen_id = self.length)[0].cyclic
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
        first_abbreviation, abbreviations = self.get_abreviations()
        linear, cyclic = self.get_oxygen()
        #for i in range(len(self.topology)):
        if len(self.topology) == 2:
            #(self.topology[0]) == "linear" and (self.topology[1]) == "cyclic":
            linear_peptides = combine_linear_smiles(first, dataset, self.length, linear)
            linear_abbreviations = combine_abbreviations(first_abbreviation, abbreviations, self.length)
            linear_library = ["linear" for _ in linear_peptides]
            cyclic_peptides = combine_cyclic_smiles(first, dataset, self.length, cyclic)
            cyclic_abbreviations = combine_abbreviations(first_abbreviation, abbreviations, self.length)
            cyclic_library = ["cyclic" for _ in cyclic_peptides]
            smiles = linear_peptides + cyclic_peptides
            ids = linear_abbreviations + cyclic_abbreviations
            libraries = linear_library + cyclic_library
            return smiles, ids, libraries
        elif (self.topology[0]) == "linear":
            linear_peptides = combine_linear_smiles(first, dataset, self.length, linear)
            linear_abbreviations = combine_abbreviations(first_abbreviation, abbreviations, self.length)
            linear_library = ["linear" for _ in linear_peptides]
            return linear_peptides, linear_abbreviations, linear_library
        elif (self.topology[0]) == "cyclic":
            cyclic_peptides = combine_cyclic_smiles(first, dataset, self.length, cyclic)
            cyclic_abbreviations = combine_abbreviations(first_abbreviation, abbreviations, self.length)
            cyclic_library = ["cyclic" for _ in cyclic_peptides]
            return cyclic_peptides, cyclic_abbreviations, cyclic_library
        else:
            return "no idea"

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
                    "MW": MW 
                }
        DF = pd.DataFrame.from_dict(data)
        return DF