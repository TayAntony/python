def novo_cadastro():
    while True:
        nome = input('Digite o nome completo: ').upper().strip()
        nasc = input('Digite sua data de nascimento (dd/mm/aaaa): ')
        print('-'*60)
        print(f'NOME = {nome}\nNASCIMENTO = {nasc}')
        confirmar = input('As informações estão corretas? [S/N] ').upper().strip()
        if confirmar == 'S':
            print('\33[32m~~~~~~~~~~~~~ CADASTRO EFETUADO COM SUCESSO ~~~~~~~~~~~~~\33[m')
            cadastros = open(r'dados_cadastrais.txt', 'a', encoding='utf-8')
            cadastros.write(f'{nome}-{nasc}\n')
            cadastros.close()
            break


def logar_adm():
    print('\33[30m\33[107m\33[1mOLÁ ADMINISTRADOR, CONFIRME SUA IDENTIDADE!\33[m')
    nome = input('Digite o nome completo: ').upper().strip()
    nasc = input('Digite sua data de nascimento (dd/mm/aaaa): ')
    adm = open(r'adm.txt', 'r', encoding='utf-8')
    admin = adm.read().split('-')
    if admin[0] == nome:
        if admin[1] == nasc:
            print('\033[1;35m>>>>>   BEM-VINDA ADM\033[0;0m')
        else:
            print('\033[1;31mDATA INCORRETA\033[0;0m')
    else:
        print('\033[1;31mNOME INCORRETO\033[0;0m')


def listar_cadastros():
    pass

def sair():
    print('\33[36m\33[4m>>>>>   Até a próxima DEV <3\33[m')

def cabecalho(txt):
    print('-'*60)
    print(txt.center(60))
    print('-'*60)
