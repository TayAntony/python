def novo_cadastro():
    nome = input('Digite o nome completo: ').upper().strip()
    nasc = input('Digite sua data de nascimento (dd/mm/aaaa): ')
    print('-'*60)
    print(f'NOME = {nome}\nNASCIMENTO = {nasc}')


def logar_adm():
    print('OLÁ ADMINISTRADOR, CONFIRME SUA IDENTIDADE!')
    nome = input('Digite o nome completo: ').upper().strip()
    nasc = input('Digite sua data de nascimento (dd/mm/aaaa): ')


def listar_cadastros():
    pass

def sair():
    print('Até a próxima DEV <3')