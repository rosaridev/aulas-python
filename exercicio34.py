#salario = float(input('qual o valor do seu salario hoje:R$ '))
#if salario > 1250:
#   print('seu salario de {}R$ com o aumento de 10%, sera: {}'.format(salario,(salario+(salario*10/100))))
#if salario <= 1250:
#    print('seu salario de {} copm o aumento de 15%, sera: {}'.format(salario,(salario+(salario*15/100))))


#agora a resolução do guanabara
salario = float(input('qual e o valro do seu salario: R$ '))
if salario<= 1250:
    novo = salario + (salario*15/100)
else:
    novo = salario + (salario*10/100)
print('quem ganhava R${:.2f} passar a ganahr R${:.2f} agora.'.format(salario,novo))