def len_2(first, dataset):
    pep2 = list(map(lambda pep: f'{first}{pep}', dataset))
    return pep2

def cyclic_len_2(first, dataset):
    print("first", first)
    _ = first.replace("N[", "N%99[")
    print("_", _)
    pep2 = list(map(lambda pep: f'{_}{pep}', dataset))
    print(pep2)
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
    #dataset = list(map(lambda x: x, dataset))
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
        pep = len_2(first, dataset)
        pep = len_3(pep,dataset)
        pep = len_4(pep, dataset)
        pep = list(map(lambda item: item + linear, pep))
        return pep
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

def combine_cyclic_smiles(first, dataset, length, cyclic):
    #dataset = list(map(lambda x: x, dataset))
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
        pep = cyclic_len_2(first, dataset)
        pep = len_3(pep,dataset)
        pep = len_4(pep, dataset)
        pep = list(map(lambda item: item + cyclic, pep))
        return pep
    elif length == 5:
        pep = cyclic_len_2(first, dataset)
        pep = len_3(pep,dataset)
        pep = len_4(pep, dataset)
        pep = len_5(pep, dataset)
        pep = list(map(lambda item: item + cyclic, pep))
        return pep
    elif length == 6:
        pep = cyclic_len_2(first, dataset)
        pep = len_3(pep,dataset)
        pep = len_4(pep, dataset)
        pep = len_5(pep, dataset)
        pep = len_6(pep, dataset)
        pep = list(map(lambda item: item + cyclic, pep))
        return pep

def combine_abbreviations(first_abbreviation, abbreviations, length):
    if length == 2:
        pep = len_2(first_abbreviation, abbreviations)
        return pep
    elif length == 3:
        pep = len_2(first_abbreviation, abbreviations)
        pep = len_3(pep,abbreviations)
        return pep
    elif length == 4:
        pep = len_2(first_abbreviation, abbreviations)
        pep = len_3(pep,abbreviations)
        pep = len_4(pep, abbreviations)
        return pep
    elif length == 5:
        pep = len_2(first_abbreviation, abbreviations)
        pep = len_3(pep,abbreviations)
        pep = len_4(pep, abbreviations)
        pep = len_5(pep, abbreviations)
        return pep
    elif length == 6:
        pep = len_2(first_abbreviation, abbreviations)
        pep = len_3(pep,abbreviations)
        pep = len_4(pep, abbreviations)
        pep = len_5(pep, abbreviations)
        pep = len_6(pep, abbreviations)
        return pep

        
#idetify reapeted strings"
#mylist = ["aa", "ab", "aa", "c", "c"]
#mylist = list(dict.fromkeys(pep))
#print(len(mylist))
