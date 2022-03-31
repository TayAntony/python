frase = input('Digite uma frase: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
'''Da para fazer o exercicio sem usar o 'for', apenas com a var 'inverso' usando fatiamento
inverso = junto[::-1]'''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('A frase {} ao contrário é {}'.format(junto,inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase não é um palíndromo!')
