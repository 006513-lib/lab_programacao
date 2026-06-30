frase = input("Digite uma frase: ")

lista = []
palavra = ""

for caractere in frase:
    if caractere != " ":
        palavra += caractere
    else:
        if palavra != "":
            lista.append(palavra)
            palavra = ""

if palavra != "":
    lista.append(palavra)

print(lista)