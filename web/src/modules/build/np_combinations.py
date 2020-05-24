import numpy as np
import multiprocessing as mp


def len_2(epep, first):
    """
    input, 
    first: amino acid at first position
    epep: element of dataset
    """
    return f"{first}{epep}"


def combine(epep, eds):
    """
    input, 
    epep: element of pep (pep is sequence from previous combination) 
    eds: element of dataset
    """
    return f"{epep}{'('}{eds}"


def combine_a(epep, eds):
    """
    generate sequence (peptides' ID)
    input,
    epep: element of pep (pep is sequence from previous combination) 
    eds: element of dataset
    """
    return f"{epep}{eds}"


def combine_smiles(dataset, length):
    """
    dataset, list with a set of amino acids
    length = int
    """
    pep = [dataset[0]]
    dataset = np.array(dataset)
    if length == 2:
        pool = mp.Pool(mp.cpu_count())
        pep2 = list()
        for eds in dataset:
            pep2 = pep2 + [pool.apply(combine, args=(epep, eds)) for epep in pep]
        pool.close()
        f_comb = pep2
    elif length == 3:
        ### 2 elements #######
        pool = mp.Pool(mp.cpu_count())
        pep2 = list()
        for eds in dataset:
            pep2 = pep2 + [pool.apply(combine, args=(epep, eds)) for epep in pep]
        pool.close()
        pep2 = np.array(pep2)
        ###### 3 elements#########
        pool = mp.Pool(mp.cpu_count())
        f_comb = list()
        for eds in dataset:
            f_comb = f_comb + [pool.apply(combine, args=(epep, eds)) for epep in pep2]
        pool.close()
    elif length == 4:
        ### 2 elements #######
        pool = mp.Pool(mp.cpu_count())
        pep2 = list()
        for eds in dataset:
            pep2 = pep2 + [pool.apply(combine, args=(epep, eds)) for epep in pep]
        pool.close()
        pep2 = np.array(pep2)
        ###### 3 elements#########
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
        pep2 = list()
        for eds in dataset:
            pep2 = pep2 + [pool.apply(combine, args=(epep, eds)) for epep in pep]
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
        pep2 = list()
        for eds in dataset:
            pep2 = pep2 + [pool.apply(combine, args=(epep, eds)) for epep in pep]
        pool.close()
        pep2 = np.array(pep2)
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


def combine_abbr(abbr, length):
    """
    abbr, list with a set of amino acids
    length = int
    """
    pep = [abbr[0]]
    abbr = np.array(abbr)
    print("abbr", abbr)
    if length == 2:
        pool = mp.Pool(mp.cpu_count())
        pep2 = list()
        for eds in abbr:
            pep2 = pep2 + [pool.apply(combine_a, args=(epep, eds)) for epep in pep]
            print("temporal pep2", pep2)
        pool.close()
        sequence = pep2
    elif length == 3:
        ### 2 elements ###
        pool = mp.Pool(mp.cpu_count())
        pep2 = list()
        for eds in abbr:
            pep2 = pep2 + [pool.apply(combine_a, args=(epep, eds)) for epep in pep]
        pool.close()
        ### 3 elements ###
        pep2 = np.array(pep2)
        pool = mp.Pool(mp.cpu_count())
        pep3 = list()
        for eds in abbr:
            pep3 = pep3 + [pool.apply(combine_a, args=(epep, eds)) for epep in pep2]
        pool.close()
        sequence = pep3
    elif length == 4:
        ### 2 elements ###
        pool = mp.Pool(mp.cpu_count())
        pep2 = list()
        for eds in abbr:
            pep2 = pep2 + [pool.apply(combine_a, args=(epep, eds)) for epep in pep]
        pool.close()
        ### 3 elements ###
        pep2 = np.array(pep2)
        pool = mp.Pool(mp.cpu_count())
        pep3 = list()
        for eds in abbr:
            pep3 = pep3 + [pool.apply(combine_a, args=(epep, eds)) for epep in pep2]
        pool.close()
        ### 4 elements ###
        pep3 = np.array(pep3)
        pool = mp.Pool(mp.cpu_count())
        sequence = list()
        for eds in abbr:
            sequence = sequence + [
                pool.apply(combine_a, args=(epep, eds)) for epep in pep3
            ]
        pool.close()
    elif length == 5:
        ### 2 elements ###
        pool = mp.Pool(mp.cpu_count())
        pep2 = list()
        for eds in abbr:
            pep2 = pep2 + [pool.apply(combine_a, args=(epep, eds)) for epep in pep]
        pool.close()
        ### 3 elements ###
        pep2 = np.array(pep2)
        pool = mp.Pool(mp.cpu_count())
        pep3 = list()
        for eds in abbr:
            pep3 = pep3 + [pool.apply(combine_a, args=(epep, eds)) for epep in pep2]
        pool.close()
        ### 4 elements ###
        pep3 = np.array(pep3)
        pool = mp.Pool(mp.cpu_count())
        pep4 = list()
        for eds in abbr:
            pep4 = pep4 + [pool.apply(combine_a, args=(epep, eds)) for epep in pep3]
        pool.close()
        ### 5 elements ###
        pep4 = np.array(pep4)
        pool = mp.Pool(mp.cpu_count())
        pep5 = list()
        for eds in abbr:
            pep5 = pep5 + [pool.apply(combine_a, args=(epep, eds)) for epep in pep4]
        pool.close()
        # pep5 = np.array(pep5)
        sequence = pep5
    elif length == 6:
        ### 2 elements ###
        pool = mp.Pool(mp.cpu_count())
        pep2 = list()
        for eds in abbr:
            pep2 = pep2 + [pool.apply(combine_a, args=(epep, eds)) for epep in pep]
        pool.close()
        ### 3 elements ###
        pep2 = np.array(pep2)
        pool = mp.Pool(mp.cpu_count())
        pep3 = list()
        for eds in abbr:
            pep3 = pep3 + [pool.apply(combine_a, args=(epep, eds)) for epep in pep2]
        pool.close()
        ### 4 elements ###
        pep3 = np.array(pep3)
        pool = mp.Pool(mp.cpu_count())
        pep4 = list()
        for eds in abbr:
            pep4 = pep4 + [pool.apply(combine_a, args=(epep, eds)) for epep in pep3]
        pool.close()
        ### 5 elements ###
        pep4 = np.array(pep4)
        pool = mp.Pool(mp.cpu_count())
        pep5 = list()
        for eds in abbr:
            pep5 = pep5 + [pool.apply(combine_a, args=(epep, eds)) for epep in pep4]
        pool.close()
        ### 6 elements ###
        pep5 = np.array(pep5)
        pool = mp.Pool(mp.cpu_count())
        pep6 = list()
        for eds in abbr:
            pep6 = pep6 + [pool.apply(combine_a, args=(epep, eds)) for epep in pep5]
        pool.close()
        sequence = pep6
    return sequence

