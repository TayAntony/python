def aumentar(moeda, taxa):
    aum = moeda + (moeda*taxa/100)
    return aum

def diminuir(moeda, taxa):
    dim = moeda - (moeda * taxa/100)
    return dim

def dobro(moeda):
    dob = moeda * 2
    return dob

def metade(moeda):
    met = moeda / 2
    return met
