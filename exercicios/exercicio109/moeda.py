def aumentar(moeda, taxa):
    aum = moeda + (moeda*taxa/100)
    return format(aum)

def diminuir(moeda, taxa):
    dim = moeda - (moeda * taxa/100)
    return format(dim)

def dobro(moeda):
    dob = moeda * 2
    return format(dob)

def metade(moeda):
    met = moeda / 2
    return format(met)

def format(preço = 0, moeda= 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')
