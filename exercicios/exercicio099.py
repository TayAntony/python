from time import sleep
def maior(* num):
    cont = maior = 0
    print('*'*50)
    print('\nAnalisando os valores informados...')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.7)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Ao todo foram informados {cont} valores!')
    print(f'Entre os valores informados o {maior} é o maior.')


maior(3, 4, 2, 8, 9, 7)
maior(2, 5, 1, 0)
maior(5, 8)
maior(7)
maior()
