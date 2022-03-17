num = int(input('Digite um número de 0 a 9999: '))
n = str(num)
unidade = num// 1 % 10
dezena = num//10 % 10
centena = num//100 % 10
milhar = num//1000 % 10
print(F'Analisando o número {num}: ')
print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')