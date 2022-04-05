'''faça um programa que recebe um número de 1 a 10 e depois faz um contagem regressiva ate 0 mostrando 1 por 1 dos numeros, se a pessoa escolher numero menor que 1 ou maior que 10 Apontar erro e encerrar o programa '''
from time import sleep
n = int(input('Digite um número de 1 a 10: '))
if n>10 or n<1:
    print('Digite um valor válido')
else:
    for n in range(n, -1, -1):
        print(n)
        sleep(1)
