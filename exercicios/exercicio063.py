print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
n = int(input('Digite a quantidade de termos que quer ver: '))
primeiro = 0
segundo = 1
print('~'*30)
print(f'{primeiro} → {segundo}',end='')
cont = 3
while cont <= n:
    terceiro = primeiro + segundo
    print(f' → {terceiro}',end='')
    primeiro = segundo
    segundo = terceiro
    cont += 1
print(' → FIM')
print('~'*30)
