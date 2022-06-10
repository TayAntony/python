def aumentar(moeda, taxa, formato=False):
    aum = moeda + (moeda*taxa/100)
    #return format(aum)     torna todas as formatações válidas sem escolher se quer ou não formatar
    return aum if formato is False else format(aum)


def diminuir(moeda, taxa, formato=False):
    dim = moeda - (moeda * taxa/100)
    #return format(dim)
    if formato is False:
        return dim
    else:
        return format(dim)


def dobro(moeda, formato=False):
    dob = moeda * 2
    #return format(dob)
    if not formato:
        return dob
    else:
        return format(dob)


def metade(moeda, formato=False):
    met = moeda / 2
    #return format(met)
    if formato == False:
        return met
    else:
        return format(met)


def format(preço = 0, moeda= 'R$'):
    return f'{moeda} {preço:.2f}'.replace('.', ',')


def resumo(valor=0 , taxa_aum=10, taxa_red=5):
    print('~' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('~' * 30)
    print(f'{"Preço analisado:":<20}{format(valor):>8}')
    print(f'{"Dobro do preço:":<20}{dobro(valor, True):>8}')
    print(f'{"Metade do preço:":<20}{metade(valor, True):>8}')
    print(f'{str(taxa_aum)+ "%" + " de aumento:":<20}{aumentar(valor, taxa_aum, True):>8}')
    print(f'{str(taxa_red)+ "%" + " de redução:":<20}{diminuir(valor, taxa_red, True):>8}')
    print('~' * 30)
