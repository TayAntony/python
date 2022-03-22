from cores import *
p = float(input('Digite o preço do produto: R$'))
desconto = (p*0.05)
total = (p-desconto)
print(f'O novo preço do produto com 5% de desconto é de: {cores["verde"]}R${total:.2f}{limpar}!')