fi = float(input('Qual o valor voce quer finaciar: '))
sl = float(input('Qual o seu salario: '))
an = int(input('em quantos anos voce quer pagar? : '))
parcela = fi / (an*12)
minimo = sl * 30/100
print('para pagar uma casa no valor de R${} em {} anos'.format(fi,an))
print('a prestaçao do financiamento ficaria R${}'.format(parcela))
if parcela <= minimo:
    print('financiamento pre aprovado!')
else:
    print('Financimaneto NEgado!')