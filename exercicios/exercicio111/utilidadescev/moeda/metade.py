def metade(moeda, formato=False):
    met = moeda / 2
    #return format(met)
    if formato == False:
        return met
    else:
        return format(met)
