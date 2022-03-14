import math
co = float(input('Digite o valor do Cateto Oposto: '))
ca = float(input('Digite o valor do Cateto Adjacente: '))
hip = math.hypot(co,ca)
print(f'O valor {co} do cateto oposto + o valor {ca} do cateto adjacente resulta na hipotenusa {hip:.2f}!')
