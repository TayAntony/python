def diminuir(moeda, taxa, formato=False):
    dim = moeda - (moeda * taxa/100)
    #return format(dim)
    if formato is False:
        return dim
    else:
        return format(dim)