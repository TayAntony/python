from cores import *
print('\033[0;97;41mOlá mundo lindo!\033[m')
print('\033[1;33;44mComo você tá? \033[m')
print('\033[1;35;43mEu estou testando cores no terminal \033[m')
print('\033[35;42mTá gostando? \033[m')
print('\033[mEsse aqui é pra ser padrão \033[m')
print('\033[0;30;107mE esse preto e branco usando a configuração atual \033[m')
#nao esquecer de colocar \033[m no final da frase dentro das aspas para indicar o final da formatação

'''usando a biblioteca de cores do vik é possível escrever as cores usando, por exemplo:
print(f'{cores ['roxo_claro']} esse é um exemplo de cor com fonte roxo claro{limpar}')

    limpar = \33[m

    cores = 
    'preto': \33[30m
    'vermelho': \33[31m
    'verde': \33[32m
    'amarelo': \33[33m
    'azul': \33[34m
    'roxo': \33[35m
    'ciano': \33[36m
    'cinza': \33[37m
    'cinza_escuro': \33[90m
    'vermelho_claro': \33[91m
    'verde_claro': \33[92m
    'amarelo_claro': \33[93m
    'azul_claro': \33[94m
    'roxo_claro': \33[95m
    'ciano_claro': \33[96m
    'branco': \33[97m


bg =
    'branco': \33[107m
    'preto': \33[40m
    'vermelho': \33[101m
    'verde': \33[102m
    'amarelo': \33[103m
    'azul': \33[104m
    'roxo': \33[105m
    'ciano': \33[106m


fx =
    'normal': \33[10m
    'contorno': \33[52m
    'negrito': \33[1m
    'italico': \33[3m
    'sublinhado': \33[4m
'''
print(f'{cores["roxo_claro"]}{bg["ciano"]}{fx["sublinhado"]}Esse é um exemplo de cor com fonte roxo claro, background ciano e sublinhado usando a biblioteca do meu namorado gênio! S2 {limpar}')