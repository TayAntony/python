from math import sin,cos,tan,radians
a = int(input('Digite um ângulo: '))
rad = radians(a)
sen = sin(rad)
co = cos(rad)
ta = tan(rad)
print(f' O seno de {a}° é {sen:.4f} \n O cosseno de {a}° é {co:.4f} \n A tangente de {a}° é {ta:.4f}')