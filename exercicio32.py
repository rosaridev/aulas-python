a = int(input('qual ano voce quer saber se e bissexto? digite o ano: '))
if a%4 == 0 and a % 100 !=0 or a %400 == 0:
    print(f'O ano {a} e bissesto!')
else:
    print(f'o ano {a} nao e bissesto!')