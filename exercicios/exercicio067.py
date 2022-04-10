while True:
    n = int(input('Digite um número para ver sua tabuada: '))
    if n <0:
        break
    else:
        print('-'*30)
        for tab in range(1,11):
            print(f'{n} x {tab:2} = {n*tab}')
        print('-'*30)
print('Tabuada encerrada!')