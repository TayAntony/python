import emoji
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print(f'A sua média foi {m:.1f}!')
if m>= 7.0:
     print('A sua média foi boa, parabéns! ',end="")
     print("\U0001F970")
else:
     print('A sua média foi ruim, estude mais! ',end="")
     print("\U0001F62C")

