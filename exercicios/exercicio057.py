sexo = str(input('Informe seu sexo: [F]/[M] ')).upper()[0].strip()
while sexo != 'M' and sexo != 'F':
    print('Por favor, indique um valor válido!')
    sexo = str(input('Qual seu sexo? [F]/[M] ')).upper()[0].strip()
print('Obrigada. Registrado com sucesso! ')
