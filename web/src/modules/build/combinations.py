def len_2(first, dataset):
    pep2 = list(map(lambda pep: f'{first}{pep}', dataset))
    return pep2

def cyclic_len_2(first, dataset):
    _ = first.replace("N[", "N%99[")
    pep2 = list(map(lambda pep: f'{_}{pep}', dataset))
    return pep2

def len_3(pep2, dataset):
    pep3 = list()
    for x0, x1 in [(x0, x1) for x0 in pep2 for x1 in dataset]:
            pep3.append(x0 + x1)
    return pep3

def len_4(pep3, dataset):
    pep4 = list()
    for x0, x1 in [(x0, x1) for x0 in pep3 for x1 in dataset]:
            pep4.append(x0 + x1)
    return pep4

def len_5(pep4, dataset):
    pep5 = list()
    for x0, x1 in [(x0, x1) for x0 in pep4 for x1 in dataset]:
            pep5.append(x0 + x1)
    return pep5
def len_6(pep5, dataset):
    pep6 = list()
    for x0, x1 in [(x0, x1) for x0 in pep5 for x1 in dataset]:
            pep6.append(x0 + x1)
    return pep6

def combine_linear_smiles(first, dataset, length, linear):
    """
    first, str with a simple amino acid
    dataset, list with a set of amino acids
    length = int
    """
    if length == 2:
        pep = len_2(first, dataset)
        pep = list(map(lambda item: item + linear, pep))
        return pep
    elif length == 3:
        pep = len_2(first, dataset)
        pep = len_3(pep,dataset)
        pep = list(map(lambda item: item + linear, pep))
        return pep
    elif length == 4:
        pep2 = len_2(first, dataset)
        pep3 = len_3(pep2,dataset)
        pep4 = len_4(pep3, dataset)
        pep4 = list(map(lambda item: item + linear, pep4))
        return pep4
    elif length == 5:
        pep = len_2(first, dataset)
        pep = len_3(pep,dataset)
        pep = len_4(pep, dataset)
        pep = len_5(pep, dataset)
        pep = list(map(lambda item: item + linear, pep))
        return pep
    elif length == 6:
        pep = len_2(first, dataset)
        pep = len_3(pep,dataset)
        pep = len_4(pep, dataset)
        pep = len_5(pep, dataset)
        pep = len_6(pep, dataset)
        pep = list(map(lambda item: item + linear, pep))
        return pep
    else:
        return "no idea"
    
def combine_cyclic_smiles(first, dataset, length, cyclic):
    """
    first, list with a simple amino acid
    dataset, list with a set of amino acids
    length = int
    """
    if length == 2:
        pep = cyclic_len_2(first, dataset)
        pep = list(map(lambda item: item + cyclic, pep))
        return pep
    elif length == 3:
        pep = cyclic_len_2(first, dataset)
        pep = len_3(pep,dataset)
        pep = list(map(lambda item: item + cyclic, pep))
        return pep
    elif length == 4:
        pep2 = cyclic_len_2(first, dataset)
        pep3 = len_3(pep2, dataset)
        pep4 = len_4(pep3, dataset)
        pep4 = list(map(lambda item: item + cyclic, pep4))
        return pep4
    elif length == 5:
        pep = cyclic_len_2(first, dataset)
        pep = len_3(pep, dataset)
        pep = len_4(pep, dataset)
        pep = len_5(pep, dataset)
        pep = list(map(lambda item: item + cyclic, pep))
        return pep
    elif length == 6:
        pep = cyclic_len_2(first, dataset)
        pep = len_3(pep, dataset)
        pep = len_4(pep, dataset)
        pep = len_5(pep, dataset)
        pep = len_6(pep, dataset)
        pep = list(map(lambda item: item + cyclic, pep))
        return pep
    else:
        return "no idea"

def combine_abbreviations(first_abbreviation, abbreviations, length):
    if length == 2:
        pep = len_2(first_abbreviation, abbreviations)
        return pep
    elif length == 3:
        pep = len_2(first_abbreviation, abbreviations)
        pep = len_3(pep,abbreviations)
        return pep
    elif length == 4:
        pep2 = len_2(first_abbreviation, abbreviations)
        pep3 = len_3(pep2, abbreviations)
        pep4 = len_4(pep3, abbreviations)
        return pep4
    elif length == 5:
        pep = len_2(first_abbreviation, abbreviations)
        pep = len_3(pep, abbreviations)
        pep = len_4(pep, abbreviations)
        pep = len_5(pep, abbreviations)
        return pep
    elif length == 6:
        pep2 = len_2(first_abbreviation, abbreviations)
        pep3 = len_3(pep2, abbreviations)
        pep4 = len_4(pep3, abbreviations)
        pep5 = len_5(pep4, abbreviations)
        pep6 = len_6(pep5, abbreviations)
        return pep6
    else:
        return "no idea :("
        
