name = str (input('Qual o seu nome: ')) # type: ignore
if name == 'Kaio':
    print('Que nome bonito!')
elif name == 'Pedro' or name == 'Abner' or name == 'Paulo':
    print('Seu nome e Biblico!')
else:
    print('Seu nome e bem popular.')
print('Tenha um bom dia, {}'.format(name))
