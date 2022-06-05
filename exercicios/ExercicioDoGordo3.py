#criar uma calculadora usando funções


def calculadora():
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))

    print('''ESCOLHA UMA OPERAÇÃO
    [1] +
    [2] -
    [3] *
    [4] /''')

    opr = int(input('Qual? '))

    resultado = executar_operacao(opr, n1, n2)
    print(resultado)


def executar_operacao(numopr, n1, n2):
    if numopr == 1:
        return soma(n1,n2)
    if numopr == 2:
        return sub(n1,n2)
    if numopr == 3:
        return mult(n1,n2)
    if numopr == 4:
        return div(n1,n2)

def soma(a, b):
    valor = a+b
    return valor

def sub(a, b):
    return a-b

def mult(a, b):
    return a*b

def div(a, b):
    return a/b

calculadora()