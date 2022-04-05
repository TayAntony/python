from time import sleep
n = int(input('Digite um número para ver seu fatorial: '))
f = 1
while n > 0:
    f = f * n
    n -= 1
print(f'{f}')

#Pode-se usar o módulo factorial da biblioteca math