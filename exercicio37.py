num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases de conversão:
[1] converte para Binário 
[2] converte para Octal
[3] converte para Hexadecimal ''')
opcao = int(input( 'sua opção: '))
if opcao == 1:
    print('a conversão do numero para Binário é: {}'.format(bin(num)[2:]))
elif opcao == 2:
    print('a conversao para Octal é igual a {}'. format(oct(num)[2:]))
elif opcao == 3:
    print('a conversao de para Hexadecimal e igual a {}'.format(hex(num) [2:]))
else:
    print('Opção invalida!')
