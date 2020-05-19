import numpy as np
import multiprocessing as mp


# def len_2(first, dataset):
#     """
#     input,
#     first:list, selected amino acids
#     output
#     pep2, np.array
#     """
#     first = np.array(first)
#     pep2 = np.core.defchararray.add(first, dataset)
#     return pep2
def len_2(epep, first):
    """
    input, 
    first: first aminoacid selected
    epep: element of dataset
    """
    return f"{first}{epep}"


def combine(epep, eds):
    """
    input, 
    eds: element of dataset
    epep: sequences from len_2 
    """
    return f"{epep}{eds}"


def len_3(epep, eds):
    return f"{epep}{eds}"


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


# def combine_smiles(first, dataset, length):
#     """
#     first, str with a simple amino acid
#     dataset, list with a set of amino acids
#     length = int
#     """
#     if length == 2:
#         pep = len_2(first, dataset)
#     elif length == 3:
#         pep = len_2(first, dataset)
#         pep = len_3(pep, dataset)
#     elif length == 4:
#         pep = len_2(first, dataset)
#         pep = pep.tolist()
#         print("type(pep)", type(pep))
#         ###paralelizacion###
#         res1 = []
#         for eds in dataset:
#             print("eds", eds)
#             # res1.append()
#             print(parallelize_func(len_3, pep, eds=eds))
#         print("total res1", res1)
#         ###
#         res1 = np.array([res1])
#         # pep = len_3(res1, dataset)
#         pep = len_4(res1, dataset)
#     elif length == 5:
#         pep = len_2(first, dataset)
#         pep = len_3(pep, dataset)
#         pep = len_4(pep, dataset)
#         pep = len_5(pep, dataset)
#     elif length == 6:
#         pep = len_2(first, dataset)
#         pep = len_3(pep, dataset)
#         pep = len_4(pep, dataset)
#         pep = len_5(pep, dataset)
#         pep = len_6(pep, dataset)
#     else:
#         pass
#     return pep


def combine_smiles(first, dataset, length):
    """
    first, str with a simple amino lengthacid
    dataset, list with a set of amino acids
    length = int
    """
    dataset = np.array(dataset)
    if length == 2:
        pool = mp.Pool(mp.cpu_count())
        f_comb = [pool.apply(len_2, args=(element, first)) for element in dataset]
        pool.close()
    elif length == 3:
        ### 2 elements #######
        pool = mp.Pool(mp.cpu_count())
        pep2 = [pool.apply(len_2, args=(element, first)) for element in dataset]
        pool.close()
        pep2 = np.array(pep2)
        ###### 3 elements#########
        pool = mp.Pool(mp.cpu_count())
        f_comb = list()
        for eds in dataset:
            f_comb = f_comb + [pool.apply(combine, args=(epep, eds)) for epep in pep2]
        pool.close()
    elif length == 4:
        ### 2 elements ###
        pool = mp.Pool(mp.cpu_count())
        pep2 = [pool.apply(len_2, args=(element, first)) for element in dataset]
        pool.close()
        ### 3 elements ###
        pep2 = np.array(pep2)
        pool = mp.Pool(mp.cpu_count())
        pep3 = list()
        for eds in dataset:
            pep3 = pep3 + [pool.apply(combine, args=(epep, eds)) for epep in pep2]
        pool.close()
        ### 4 elements ###
        pep3 = np.array(pep3)
        pool = mp.Pool(mp.cpu_count())
        f_comb = list()
        for eds in dataset:
            f_comb = f_comb + [pool.apply(combine, args=(epep, eds)) for epep in pep3]
        pool.close()
    elif length == 5:
        ### 2 elements ###
        pool = mp.Pool(mp.cpu_count())
        pep2 = [pool.apply(len_2, args=(element, first)) for element in dataset]
        pool.close()
        ### 3 elements ###
        pep2 = np.array(pep2)
        pool = mp.Pool(mp.cpu_count())
        pep3 = list()
        for eds in dataset:
            pep3 = pep3 + [pool.apply(combine, args=(epep, eds)) for epep in pep2]
        pool.close()
        ### 4 elements ###
        pep3 = np.array(pep3)
        pool = mp.Pool(mp.cpu_count())
        pep4 = list()
        for eds in dataset:
            pep4 = pep4 + [pool.apply(combine, args=(epep, eds)) for epep in pep3]
        pool.close()
        ### 5 elements ###
        pep4 = np.array(pep4)
        pool = mp.Pool(mp.cpu_count())
        pep5 = list()
        for eds in dataset:
            pep5 = pep5 + [pool.apply(combine, args=(epep, eds)) for epep in pep4]
        pool.close()
        # pep5 = np.array(pep5)
        f_comb = pep5
    elif length == 6:
        ### 2 elements ###
        pool = mp.Pool(mp.cpu_count())
        pep2 = [pool.apply(len_2, args=(element, first)) for element in dataset]
        pool.close()
        ### 3 elements ###
        pep2 = np.array(pep2)
        pool = mp.Pool(mp.cpu_count())
        pep3 = list()
        for eds in dataset:
            pep3 = pep3 + [pool.apply(combine, args=(epep, eds)) for epep in pep2]
        pool.close()
        ### 4 elements ###
        pep3 = np.array(pep3)
        pool = mp.Pool(mp.cpu_count())
        pep4 = list()
        for eds in dataset:
            pep4 = pep4 + [pool.apply(combine, args=(epep, eds)) for epep in pep3]
        pool.close()
        ### 5 elements ###
        pep4 = np.array(pep4)
        pool = mp.Pool(mp.cpu_count())
        pep5 = list()
        for eds in dataset:
            pep5 = pep5 + [pool.apply(combine, args=(epep, eds)) for epep in pep4]
        pool.close()
        # pep5 = np.array(pep5)
        f_comb = pep5
        ### 6 elements ###
        pep5 = np.array(pep5)
        pool = mp.Pool(mp.cpu_count())
        pep6 = list()
        for eds in dataset:
            pep6 = pep6 + [pool.apply(combine, args=(epep, eds)) for epep in pep5]
        pool.close()
        # pep5 = np.array(pep5)
        f_comb = pep6
    return f_comb


def combine_linear_smiles(f_comb, length, linear):
    if length == 2:
        linear_smiles = list(map(lambda item: item + linear, f_comb))
    elif length == 3:
        linear_smiles = list(map(lambda item: item + linear, f_comb))
    elif length == 4:
        linear_smiles = list(map(lambda item: item + linear, f_comb))
    elif length == 5:
        linear_smiles = list(map(lambda item: item + linear, f_comb))
    elif length == 6:
        linear_smiles = list(map(lambda item: item + linear, f_comb))
    else:
        pass
    return linear_smiles


def combine_cyclic_smiles(f_comb, length, cyclic):
    """
    
    """
    if length == 2:
        pep = list(map(lambda p: f'{"st"}{p}', f_comb))
        pep = list(map(lambda p: p.replace("stN[", "N%99["), pep))
        cyclic_smiles = list(map(lambda item: item + cyclic, pep))
    elif length == 3:
        pep = list(map(lambda p: f'{"st"}{p}', f_comb))
        pep = list(map(lambda p: p.replace("stN[", "N%99["), pep))
        cyclic_smiles = list(map(lambda item: item + cyclic, pep))
    elif length == 4:
        pep = list(map(lambda p: f'{"st"}{p}', f_comb))
        pep = list(map(lambda p: p.replace("stN[", "N%99["), pep))
        cyclic_smiles = list(map(lambda item: item + cyclic, pep))
    elif length == 5:
        pep = list(map(lambda p: f'{"st"}{p}', f_comb))
        pep = list(map(lambda p: p.replace("stN[", "N%99["), pep))
        cyclic_smiles = list(map(lambda item: item + cyclic, pep))
    elif length == 6:
        pep = list(map(lambda p: f'{"st"}{p}', f_comb))
        pep = list(map(lambda p: p.replace("stN[", "N%99["), pep))
        cyclic_smiles = list(map(lambda item: item + cyclic, pep))
    else:
        pass
    return cyclic_smiles


def combine_abbr(first_ab, abbr, length):
    """
    first_ab, str with a simple amino lengthacid
    abbr, list with a set of amino acids
    length = int
    """
    abbr = np.array(abbr)
    print("abbr", abbr)
    if length == 2:
        pool = mp.Pool(mp.cpu_count())
        f_comb = [pool.apply(len_2, args=(element, first_ab)) for element in abbr]
        pool.close()
    elif length == 3:
        ### 2 elements #######
        pool = mp.Pool(mp.cpu_count())
        pep2 = [pool.apply(len_2, args=(element, first)) for element in abbr]
        pool.close()
        pep2 = np.array(pep2)
        ###### 3 elements#########
        pool = mp.Pool(mp.cpu_count())
        f_comb = list()
        for eds in abbr:
            f_comb = f_comb + [pool.apply(combine, args=(epep, eds)) for epep in pep2]
        pool.close()
    elif length == 4:
        ### 2 elements ###
        pool = mp.Pool(mp.cpu_count())
        pep2 = [pool.apply(len_2, args=(element, first_ab)) for element in abbr]
        pool.close()
        ### 3 elements ###
        pep2 = np.array(pep2)
        pool = mp.Pool(mp.cpu_count())
        pep3 = list()
        for eds in abbr:
            pep3 = pep3 + [pool.apply(combine, args=(epep, eds)) for epep in pep2]
        pool.close()
        ### 4 elements ###
        pep3 = np.array(pep3)
        pool = mp.Pool(mp.cpu_count())
        sequence = list()
        for eds in abbr:
            sequence = sequence + [
                pool.apply(combine, args=(epep, eds)) for epep in pep3
            ]
        pool.close()
    elif length == 5:
        ### 2 elements ###
        pool = mp.Pool(mp.cpu_count())
        pep2 = [pool.apply(len_2, args=(element, first_ab)) for element in abbr]
        pool.close()
        ### 3 elements ###
        pep2 = np.array(pep2)
        pool = mp.Pool(mp.cpu_count())
        pep3 = list()
        for eds in abbr:
            pep3 = pep3 + [pool.apply(combine, args=(epep, eds)) for epep in pep2]
        pool.close()
        ### 4 elements ###
        pep3 = np.array(pep3)
        pool = mp.Pool(mp.cpu_count())
        pep4 = list()
        for eds in abbr:
            pep4 = pep4 + [pool.apply(combine, args=(epep, eds)) for epep in pep3]
        pool.close()
        ### 5 elements ###
        pep4 = np.array(pep4)
        pool = mp.Pool(mp.cpu_count())
        pep5 = list()
        for eds in abbr:
            pep5 = pep5 + [pool.apply(combine, args=(epep, eds)) for epep in pep4]
        pool.close()
        # pep5 = np.array(pep5)
        sequence = pep5
    elif length == 6:
        ### 2 elements ###
        pool = mp.Pool(mp.cpu_count())
        pep2 = [pool.apply(len_2, args=(element, first_ab)) for element in abbr]
        pool.close()
        ### 3 elements ###
        pep2 = np.array(pep2)
        pool = mp.Pool(mp.cpu_count())
        pep3 = list()
        for eds in abbr:
            pep3 = pep3 + [pool.apply(combine, args=(epep, eds)) for epep in pep2]
        pool.close()
        ### 4 elements ###
        pep3 = np.array(pep3)
        pool = mp.Pool(mp.cpu_count())
        pep4 = list()
        for eds in abbr:
            pep4 = pep4 + [pool.apply(combine, args=(epep, eds)) for epep in pep3]
        pool.close()
        ### 5 elements ###
        pep4 = np.array(pep4)
        pool = mp.Pool(mp.cpu_count())
        pep5 = list()
        for eds in abbr:
            pep5 = pep5 + [pool.apply(combine, args=(epep, eds)) for epep in pep4]
        pool.close()
        # pep5 = np.array(pep5)
        f_comb = pep5
        ### 6 elements ###
        pep5 = np.array(pep5)
        pool = mp.Pool(mp.cpu_count())
        pep6 = list()
        for eds in abbr:
            pep6 = pep6 + [pool.apply(combine, args=(epep, eds)) for epep in pep5]
        pool.close()
        # pep5 = np.array(pep5)
        sequence = pep6
    return sequence
    # if length == 2:
    #     sequence = len_2(first_abbreviation, abbr)
    # elif length == 3:
    #     pep = len_2(first_abbreviation, abbr)
    #     sequence = len_3(pep, abbr)
    # elif length == 4:
    #     pep = len_2(first_abbreviation, abbr)
    #     pep = len_3(pep, abbr)
    #     sequence = len_4(pep, abbr)
    # elif length == 5:
    #     pep = len_2(first_abbreviation, abbr)
    #     pep = len_3(pep, abbr)
    #     pep = len_4(pep, abbr)
    #     sequence = len_5(pep, abbr)
    # elif length == 6:
    #     pep = len_2(first_abbreviation, abbr)
    #     pep = len_3(pep, abbr)
    #     pep = len_4(pep, abbr)
    #     pep = len_5(pep, abbr)
    #     sequence = len_6(pep, abbr)
    # else:
    #     pass
    # return sequence.tolist()
