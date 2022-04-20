palavras = ('APRENDER','PROGRAMAR','PYHTON','CURSO','EVOLUIR','ENSINAR','PRATICAR','ESTUDAR','AMOR','FELICIDADE','VIVER')
for p in palavras:
    print(f'\nNa palavra {p} temos: ', end='')
    for letra in p:
        if letra in 'AEIOU':
            print(letra, end=' ')