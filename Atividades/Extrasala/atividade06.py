nomes = []
nomes_invertidos = []
for i in range(1,6):
    n = input(f'digite o {i}° nome: ')
    nomes.append(n)

nomes_invertidos.append(nomes)
nomes_invertidos = nomes[::-1]

print(f'lista: {nomes}')
print(f'lista invertida: {nomes_invertidos}')