def voto(ano):
    from datetime import datetime
    atual = datetime.now().year
    idade = atual - ano
    if idade < 16:
        return f'Você tem {idade} anos: NÃO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        return f'Você tem {idade} anos: VOTO OPCIONAL'
    elif ano > 18:
        return f'Você tem {idade} anos: VOTO OBRIGATÓRIO'


nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
