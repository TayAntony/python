print(f'{" LOJA DA TAY ":=^30}')
produto = float(input('Digite o valor do produto: R$'))
dinheiro = produto*0.1
cartao = produto*0.05
cartao3 = produto*0.2
print('''Qual a forma de pagamento?
[ 1 ] À vista dinheiro/cheque
[ 2 ] À vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
resposta = int(input('Digite sua opção: '))
if resposta == 1:
    print(f'À vista no dinheiro ou cheque o produto tem 10% de desconto, passando de R${produto:.2f} para R${produto-dinheiro:.2f}. Aproveite!')
elif resposta == 2:
    print(f'À vista no cartão o produto tem 5% de desconto, passando de R${produto:.2f} para R${produto-cartao:.2f}. Aproveite!')
elif resposta == 3:
    print(f'Em até 2x no cartão o produto tem o preço normal que é de R${produto:.2f}')
elif resposta == 4:
    print(f'Em 3x ou mais no cartão o produto tem 20% de juros, passando de R${produto:.2f} para R${produto+cartao3:.2f}')
else:
    print('Opção inválida. Tente novamente!')