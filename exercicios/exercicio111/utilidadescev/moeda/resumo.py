from .diminuir import diminuir
from .aumentar import aumentar
from .dobro import dobro
from .metade import metade

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