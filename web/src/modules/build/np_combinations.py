import numpy as np


def len_2(first, dataset):
    """
    input, 
    first:list, selected amino acids
    output
    pep2, np.array
    """
    first = np.array(first)
    pep2 = np.core.defchararray.add(first, dataset)
    return pep2


def len_3(pep2, dataset):
    pep3 = np.empty(0)
    for i in dataset:
        peps = np.core.defchararray.add(pep2, np.array(i))
        pep3 = np.concatenate((pep3, peps), axis=None)
    return pep3


def len_4(pep3, dataset):
    pep4 = np.empty(0)
    for i in dataset:
        i = np.core.defchararray.add(pep3, np.array(i))
        pep4 = np.concatenate((pep4, i), axis=None)
    return pep4


def len_5(pep4, dataset):
    pep5 = np.empty(0)
    for i in dataset:
        i = np.core.defchararray.add(pep4, np.array(i))
        pep5 = np.concatenate((pep5, i), axis=None)
    return pep5


def len_6(pep5, dataset):
    pep6 = np.empty(0)
    for i in dataset:
        i = np.core.defchararray.add(pep5, np.array(i))
        pep6 = np.concatenate((pep6, i), axis=None)
    return pep6


def combine_smiles(first, dataset, length):
    """
    first, str with a simple amino acid
    dataset, list with a set of amino acids
    length = int
    """
    if length == 2:
        pep = len_2(first, dataset)
    elif length == 3:
        pep = len_2(first, dataset)
        pep = len_3(pep, dataset)
    elif length == 4:
        pep = len_2(first, dataset)
        pep = len_3(pep, dataset)
        pep = len_4(pep, dataset)
    elif length == 5:
        pep = len_2(first, dataset)
        pep = len_3(pep, dataset)
        pep = len_4(pep, dataset)
        pep = len_5(pep, dataset)
    elif length == 6:
        pep = len_2(first, dataset)
        pep = len_3(pep, dataset)
        pep = len_4(pep, dataset)
        pep = len_5(pep, dataset)
        pep = len_6(pep, dataset)
    else:
        pass
    return pep


def combine_linear_smiles(pep, length, linear):
    if length == 2:
        linear_smiles = list(map(lambda item: item + linear, pep.tolist()))
    elif length == 3:
        linear_smiles = list(map(lambda item: item + linear, pep.tolist()))
    elif length == 4:
        linear_smiles = list(map(lambda item: item + linear, pep.tolist()))
    elif length == 5:
        linear_smiles = list(map(lambda item: item + linear, pep.tolist()))
    elif length == 6:
        linear_smiles = list(map(lambda item: item + linear, pep.tolist()))
    else:
        pass
    return linear_smiles


def combine_cyclic_smiles(pep, length, cyclic):
    """
    first, list with a simple amino acid
    dataset, list with a set of amino acids
    length = int
    """
    if length == 2:
        pep = pep.tolist()
        pep = list(map(lambda p: f'{"st"}{p}', pep))
        pep = list(map(lambda p: p.replace("stN[", "N%99["), pep))
        cyclic_smiles = list(map(lambda item: item + cyclic, pep))
    elif length == 3:
        pep = pep.tolist()
        pep = list(map(lambda p: f'{"st"}{p}', pep))
        pep = list(map(lambda p: p.replace("stN[", "N%99["), pep))
        cyclic_smiles = list(map(lambda item: item + cyclic, pep))
    elif length == 4:
        pep = pep.tolist()
        pep = list(map(lambda p: f'{"st"}{p}', pep))
        pep = list(map(lambda p: p.replace("stN[", "N%99["), pep))
        cyclic_smiles = list(map(lambda item: item + cyclic, pep))
    elif length == 5:
        pep = pep.tolist()
        pep = list(map(lambda p: f'{"st"}{p}', pep))
        pep = list(map(lambda p: p.replace("stN[", "N%99["), pep))
        cyclic_smiles = list(map(lambda item: item + cyclic, pep))
    elif length == 6:
        pep = pep.tolist()
        pep = list(map(lambda p: f'{"st"}{p}', pep))
        pep = list(map(lambda p: p.replace("stN[", "N%99["), pep))
        cyclic_smiles = list(map(lambda item: item + cyclic, pep))
    else:
        pass
    return cyclic_smiles


def combine_abbr(first_abbreviation, abbr, length):
    if length == 2:
        sequence = len_2(first_abbreviation, abbr)
    elif length == 3:
        pep = len_2(first_abbreviation, abbr)
        sequence = len_3(pep, abbr)
    elif length == 4:
        pep = len_2(first_abbreviation, abbr)
        pep = len_3(pep, abbr)
        sequence = len_4(pep, abbr)
    elif length == 5:
        pep = len_2(first_abbreviation, abbr)
        pep = len_3(pep, abbr)
        pep = len_4(pep, abbr)
        sequence = len_5(pep, abbr)
    elif length == 6:
        pep = len_2(first_abbreviation, abbr)
        pep = len_3(pep, abbr)
        pep = len_4(pep, abbr)
        pep = len_5(pep, abbr)
        sequence = len_6(pep, abbr)
    else:
        pass
    return sequence.tolist()
