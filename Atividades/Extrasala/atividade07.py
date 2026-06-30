pares = []
impares = []

while len(pares) + len(impares) < 10:
    numero = int(input("Digite um número inteiro: "))

    if numero in pares or numero in impares:
        print("Esse já foi! Tenta outro.")
        continue
    
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Lista de pares:", pares)
print("Lista de ímpares:", impares)