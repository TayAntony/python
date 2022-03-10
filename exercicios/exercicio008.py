m = float(input('Escreva um valor em metros: '))
km = m//1000
hm = m//100
dam = m//10
dm = m*10
c = m*100
mili = m*1000
print(f'{m:.1f} metros tem {c:.0f} centímetros \n {mili:.0f} milímetros \n {dm} decímetros \n {dam} decâmetros \n {hm} hectômetros \n {km} quilômetros')