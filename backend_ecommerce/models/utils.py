def transform_tramo_discount(lista):
    """
    Function to transform a list like this [10,50,200] (limit in discount tramos)
    into this [[10,11,12,........,49], [50,51,52,.......,199],[200,201,..........,1000]]
    A upper-limit has considered as 1000
    :param lista:
    :return:
    """
    ranges = []
    for idx, item in enumerate(lista):
        ini = item
        if idx != len(lista) - 1:
            fin = lista[idx + 1: idx + 2][0]
        else:
            fin = 1000
        ranges.append(list(range(ini, fin)))
    return ranges