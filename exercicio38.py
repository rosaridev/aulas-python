from datetime import date
atual = date.today().year
an = int(input('qual Ano vocé nasceu?: '))
sexo = input('Seu sexo e masculino ou feminino: ').strip().lower()  
idade = atual - an
print( 'Quem nasceu em {} tem {} anos em {}'.format(an,idade,atual))
if sexo == 'masculino':
    if idade == 18:
        print('Deve se alistar ate o final do ano!')
        print('seu alistamento e obrigatorio')
    elif idade < 18:
        saldo = 18 - idade
        ano = atual + saldo
        print('ainda falta {} anos para seu alsitamento!'.format(saldo)) 
        print('Seu ano de alistamento sera: {} '.format(ano))
    elif idade > 18:# eu poderia colocar o else que iria fucionar normalmente.
        saldo = idade - 18
        ano = atual - saldo
        print('Voce ja deveria ter se alstado ha {} anos. '.format(saldo))
        print('Seu ano de alstamento foi: {} '.format(ano))
elif sexo == 'feminino':
    
    print('O alistamento militar não é obrigatório para mulheres.')
else:
    
    print('Sexo inválido. Digite "masculino" ou "feminino".')
