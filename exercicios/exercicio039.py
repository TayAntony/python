from datetime import date
atual = date.today().year
nasc = int(input('Qual seu ano de nascimento? '))
idade = atual - nasc
print('''Qual seu sexo? 
Feminino
Masculino''')
sexo = input('Sua opção:')
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}!')
if sexo=='feminino':
    print('Parabéns minha consagrada, você não precisa fazer alistamento militar obrigatório!')
elif idade == 18:
    print('Você tem que se alistar imediatamente!!')
elif idade < 18:
    saldo = 18 - idade
    ano  = atual + saldo
    print(f'Ainda faltam {saldo} ano(s) para o seu alistamento.')
    print(f'Seu alistamento será em {ano}')
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print(f'Você deveria ter se alistado há {saldo} ano(s).')
    print(f'Seu alistamento foi em {ano}')
