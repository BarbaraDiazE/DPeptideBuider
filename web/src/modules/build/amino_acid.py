"""Data"""
dict_amino_acid = {
                    "ALA": {
                                "name": "ALA",
                                "first_smile": "N[C@@H](C)C",
                                "first_abbreviation": "A",
                                "linear_smile" : "(N[C@@H](C)C",
                                "linear_abbreviation" : "A",
                                "methylated_smile": "(N(C)[C@@H](C)C",
                                "methylated_abbreviation": "A(M)"
                            },
                    "CYS":{
                                "name": "CYS",
                                "first_smile": "N[C@@H](CS)C",
                                "first_abbreviation": "C",
                                "linear_smile" : "(N[C@@H](CS)C",
                                "linear_abbreviation" : "C",
                                "methylated_smile": "(N(C)[C@@H](CS)C",
                                "methylated_abbreviation": "C(M)"
                            },
                    "ASP":{
                                "name": "ASP",
                                "first_smile": "N[C@H](C(O)O)CC",
                                "first_abbreviation": "D",
                                "linear_smile" : "(N[C@H](C(O)O)CC",
                                "linear_abbreviation" : "D",
                                "methylated_smile": "(N(C)[C@H](C(O)O)CC",
                                "methylated_abbreviation": "D(M)"
                            },
                    "GLU":{
                                "name": "GLU",
                                "first_smile": "N[C@H](C(O)O)CCC",
                                "first_abbreviation": "E",
                                "linear_smile" : "(N[C@H](C(O)O)CCC",
                                "linear_abbreviation" : "E",
                                "methylated_smile": "(N(C)[C@H](C(O)O)CCC",
                                "methylated_abbreviation": "E(M)"
                            },
                    "PHE":{
                                "name": "PHE",
                                "first_smile": "N[C@@H](Cc3ccccc3)C",
                                "first_abbreviation": "F",
                                "linear_smile" : "(N[C@@H](Cc3ccccc3)C",
                                "linear_abbreviation" : "F",
                                "methylated_smile": "(N(C)[C@@H](Cc3ccccc3)C",
                                "methylated_abbreviation": "F(M)"
                            },
                    "HIS":{
                                "name": "HIS",
                                "first_smile": "N[C@@H](Cc4[nH]cnc4)C",
                                "first_abbreviation": "H",
                                "linear_smile" : "(N[C@@H](Cc4[nH]cnc4)C",
                                "linear_abbreviation" : "H",
                                "methylated_smile": "(N(C)[C@@H](Cc4[nH]cnc4)C",
                                "methylated_abbreviation": "H(M)"
                            },
                    "ILE":{
                                "name": "ILE",
                                "first_smile": "N[C@@H]([C@@H](C)CC)C",
                                "first_abbreviation": "I",
                                "linear_smile" : "(N[C@@H]([C@@H](C)CC)C",
                                "linear_abbreviation" : "I",
                                "methylated_smile": "(N(C)[C@@H]([C@@H](C)CC)C",
                                "methylated_abbreviation": "I"
                            },
                    "LYS":{
                                "name": "LYS",
                                "first_smile": "N[C@@H](CCCCN)C",
                                "first_abbreviation": "K",
                                "linear_smile" : "(N[C@@H](CCCCN)C",
                                "linear_abbreviation" : "K",
                                "methylated_smile": "(N(C)[C@@H](CCCCN)C",
                                "methylated_abbreviation": "K(M)"
                            },
                    "LEU":{
                                "name": "LEU",
                                "first_smile": "N[C@@H](CC(C)C)C",
                                "first_abbreviation": "L",
                                "linear_smile" : "(N[C@@H](CC(C)C)C",
                                "linear_abbreviation" : "L",
                                "methylated_smile": "(N(C)[C@@H](CC(C)C)C",
                                "methylated_abbreviation": "L(M)"
                            },
                    "MET":{
                                "name": "MET",
                                "first_smile": "N[C@@H](CCSC)C",
                                "first_abbreviation": "M",
                                "linear_smile" : "(N[C@@H](CCSC)C",
                                "linear_abbreviation" : "M",
                                "methylated_smile": "(N[C@@H](CCSC)C",
                                "methylated_abbreviation": "M(M)"
                            },
                    "ASN":{
                                "name": "ASN",
                                "first_smile": "N[C@@H](CC(N)O)C",
                                "first_abbreviation": "N",
                                "linear_smile" : "(N[C@@H](CC(N)O)C",
                                "linear_abbreviation" : "N",
                                "methylated_smile": "(N(C)[C@@H](CC(N)O)C",
                                "methylated_abbreviation": "N(M)"
                            },
                    "PRO":{
                                "name": "PRO",
                                "first_smile": "N1CCC[C@H]1C",
                                "first_abbreviation": "P",
                                "linear_smile" : "(N1CCC[C@H]1C",
                                "linear_abbreviation" : "P",
                                "methylated_smile": "(N1(C)CCC[C@H]1C",
                                "methylated_abbreviation": "P"
                            },
                    "GLN":{
                                "name": "GLN",
                                "first_smile": "N[C@@H](CCC(N)O)C",
                                "first_abbreviation": "Q",
                                "linear_smile" : "(N[C@@H](CCC(N)O)C",
                                "linear_abbreviation" : "Q",
                                "methylated_smile": "(N(C)[C@@H](CCC(N)O)C",
                                "methylated_abbreviation": "Q"
                            },
                    "ARG":{
                                "name": "ARG",
                                "first_smile": "N[C@@H](CCCNC(N)N)C",
                                "first_abbreviation": "R",
                                "linear_smile" : "(N[C@@H](CCCNC(N)N)C",
                                "linear_abbreviation" : "R",
                                "methylated_smile": "(N(C)[C@@H](CCCNC(N)N)C",
                                "methylated_abbreviation": "R(M)"
                            },
                    "SER":{
                                "name": "SER",
                                "first_smile": "N[C@@H](CO)C",
                                "first_abbreviation": "S",
                                "linear_smile" : "(N[C@@H](CO)C",
                                "linear_abbreviation" : "S",
                                "methylated_smile": "(N(C)[C@@H](CO)C",
                                "methylated_abbreviation": "S(M)"
                            },
                    "THR":{
                                "name": "THR",
                                "first_smile": "N[C@@H]([C@H](O)C)C",
                                "first_abbreviation": "T",
                                "linear_smile" : "(N[C@@H]([C@H](O)C)C",
                                "linear_abbreviation" : "T",
                                "methylated_smile": "(N(C)[C@@H]([C@H](O)C)C",
                                "methylated_abbreviation": "T(M)"
                            },
                    "VAL":{
                                "name": "VAL",
                                "first_smile": "N[C@@H](C(C)C)C",
                                "first_abbreviation": "V",
                                "linear_smile" : "(N[C@@H](C(C)C)C",
                                "linear_abbreviation" : "V",
                                "methylated_smile": "(N(C)[C@@H](C(C)C)C",
                                "methylated_abbreviation": "V(M)"
                            },
                    "TRP":{
                                "name": "TRP",
                                "first_smile": "N[C@@H](Cc5c[nH]c6c5cccc6)C",
                                "first_abbreviation": "W",
                                "linear_smile" : "(N[C@@H](Cc5c[nH]c6c5cccc6)C",
                                "linear_abbreviation" : "W",
                                "methylated_smile": "(N(C)[C@@H](Cc5c[nH]c6c5cccc6)C",
                                "methylated_abbreviation": "W(M)"
                            },
                    "TYR":{
                                "name": "TYR",
                                "first_smile": "N[C@@H](Cc7ccc(O)cc7)C",
                                "first_abbreviation": "Y",
                                "linear_smile" : "(N[C@@H](Cc7ccc(O)cc7)C",
                                "linear_abbreviation" : "Y",
                                "methylated_smile": "(N(C)[C@@H](Cc7ccc(O)cc7)C",
                                "methylated_abbreviation": "Y(M)"
                            },
                    "GLY":{
                                "name": "GLY",
                                "first_smile": "NCC",
                                "first_abbreviation": "G",
                                "linear_smile" : "(NCC",
                                "linear_abbreviation" : "G",
                                "methylated_smile": "(N(C)CC",
                                "methylated_abbreviation": "G(M)"
                            },
                }

