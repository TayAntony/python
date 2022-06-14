from .formatacao import formatacao
from .diminuir import diminuir
from .aumentar import aumentar
from .dobro import dobro
from .metade import metade

def resumo(valor=0 , taxa_aum=10, taxa_red=5):
    print('~' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('~' * 30)
    print(f'{"Preço analisado:":<20}{formatacao(valor):>6}')
    print(f'{"Dobro do preço:":<20}{formatacao(dobro(valor, True)):>6}')
    print(f'{"Metade do preço:":<20}{formatacao(metade(valor, True)):>6}')
    print(f'{str(taxa_aum)+ "%" + " de aumento:":<20}{formatacao(aumentar(valor, taxa_aum, True)):>6}')
    print(f'{str(taxa_red)+ "%" + " de redução:":<20}{formatacao(diminuir(valor, taxa_red, True)):>6}')
    print('~' * 30)
