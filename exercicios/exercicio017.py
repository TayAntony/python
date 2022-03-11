import math
co = int(input('Digite o valor do Cateto Oposto: '))
ca = int(input('Digite o valor do Cateto Adjacente: '))
hip = math.sqrt(co**2+ca**2)
print(f'O valor {co} do cateto oposto + o valor {ca} do cateto adjacente resulta na hipotenusa {hip:.2f}!')