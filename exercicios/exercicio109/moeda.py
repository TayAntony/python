def aumentar(moeda, taxa, formato=False):
    aum = moeda + (moeda*taxa/100)
    #return format(aum)     torna todas as formatações válidas sem escolher se quer ou não formatar
    return aum if formato is False else moeda(aum)

def diminuir(moeda, taxa, formato=False):
    dim = moeda - (moeda * taxa/100)
    #return format(dim)
    return dim if formato is False else moeda(dim)

def dobro(moeda, formato=False):
    dob = moeda * 2
    #return format(dob)
    return dob if formato is False else moeda(dob)

def metade(moeda, formato=False):
    met = moeda / 2
    #return format(met)
    return met if formato is False else moeda(met)

def format(preço = 0, moeda= 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')
