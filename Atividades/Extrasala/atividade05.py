lista = []

for i in range(1,7):
    v = int(input(f'digite o {i}° numero: '))
    lista.append(v)
num = int(input('digite o número teste: '))

cont = lista.count(num)

print(f'o numero buscado aparece {cont} vezes')
if cont > 0:
    posição = lista.index(num)
    print(f'ele aparece em {posição + 1}° lugar.')