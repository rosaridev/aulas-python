print('-='*20)
print('Analisador de Trangulos!')
print('-='*20)
n1 = float(input('escolha um segmento da primeira reta: '))
n2 = float(input('a segunda reta: '))
n3 = float(input('a terceira reta: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print(' e possivel virar um triangulo!')


else:
    print('nao e possivel transfoprma em um triangulo!')