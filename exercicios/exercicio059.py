from time import sleep
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS VALORES
    [ 5 ] SAIR''')
    opcao = int(input('>>>>> O que deseja fazer com os valores? '))
    if opcao == 1:
        soma = n1+n2
        print(f'A soma entre {n1} e {n2} é {soma}')
    elif opcao == 2:
        mult = n1*n2
        print(f'A multiplicação de {n1} x {n2} é {mult}')
    elif opcao == 3:
        if n1>n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior é {maior}')
    elif opcao == 4:
        print('Informe os números novamente')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: ')) 
    elif opcao == 5:
        print('Finalizando...')
    else: 
        print('Opção inválida. Tente novamente.')
    print('-='*15)
    sleep(2)  
print('Fim do programa! Volte sempre.')
