def fatorial(n, show=False):
    """
     -> Calcula o fatorial de um número:
    parâmetro n = O número a ser calculado.
    parâmetro show =  (opcional) Mostrar ou não a conta.
    return: O valor do fatorial de um número n.
    """

    f = 1
    for c in range (n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

fat = int(input('Digite um número para ver seu fatorial: '))
print(fatorial(fat, show=False))
#help(fatorial)
