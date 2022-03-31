print('='*50)
print('10 TERMOS DE UMA PROGRESSÃO ARITMÉTICA')
print('='*50)
pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))
u = pt+10*r
for c in range(pt, u, r):
    print(c, end=' → ')
print('ACABOU')