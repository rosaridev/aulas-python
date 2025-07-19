a = int(input('primeiro valor: '))
b = int(input('segundo numero: '))
c = int(input('terciero valor: '))
menor = a
if b<a and b<c:
    menor = b
if c<b and c<a:
    menor = c
print(' o menor valor e o {}'.format(menor))