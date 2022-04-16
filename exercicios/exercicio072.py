sequencia = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
    pergunta = int(input('Digite um número entre 0 e 20: '))
    if pergunta <0 or pergunta >20:
        print('Tente novamente...',end='') 
    if pergunta >= 0 and pergunta <=20:
        print(f'Você digitou o número {sequencia[pergunta]}!')
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar in 'Ss':
        continue
    if continuar in 'Nn':
        print('Programa encerrado. Volte sempre!')
    break
