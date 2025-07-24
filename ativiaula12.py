name = str (input('Qual o seu nome: ')) # type: ignore
if name == 'Kaio':
    print('Que nome bonito!')
elif name == 'Pedro' or name == 'Abner' or name == 'Paulo':
    print('Seu nome e Biblico!')
elif name in 'jennifer ana claudia rose':
    print(' nomes femeninos')
else:
    print('Seu nome e bem popular.')
print('Tenha um bom dia, {}'.format(name))
