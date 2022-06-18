import urllib
import urllib.request # o request é um módulo interno da urllib

try:
    site=urllib.request.urlopen('http://www.pudim.com.br')
#urlopen é para tentar abrir a url dentro dos parenteses e aspas

except urllib.request.URLError:
    print('O site PUDIM não está acessível no momento :(')
else:
    print('O site PUDIM está acessíVel :D')
    print(site.read())
    #o código do site (que é bem simples)

# except é para quando dar erro
# else é para quando da certo
