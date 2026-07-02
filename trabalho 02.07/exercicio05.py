nome = input('Digite seu nome: ')

resultado = ''
comecopala = True

for letra in nome:
    if letra != ' ':
        if comecopala:
            resultado += letra + '. '
            comecopala = False
    else:
        comecopala = True

print(f'As inicias são: {resultado}')