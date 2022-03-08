n = input('Digite qualquer coisa: ')
print(f'É do tipo: {type(n)}')
print(f'É um número? {n.isnumeric()}')
print(f'É uma letra? {n.isalpha()}')
print(f'É um alfanumérico? {n.isalnum()}')
print(f'Está tudo maiúsculo? {n.isupper()}')
print(f'Está tudo minúsculo? {n.islower()}')
print(f'Só tem espaços? {n.isspace()}')
print(f'Está capitalizada? {n.istitle()}')


