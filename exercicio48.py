#for n in range(1,501):
#    if n % 2 ==1:
#       print(n)       

soma = 0
cont = 0
for c in range (1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
    
print(' a somas de todos os valores {} que são impares multiplos de 3 é: {}'.format(cont,soma))