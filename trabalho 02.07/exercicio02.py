frase = input('Digite uma frase: ').lower()

somapalavra = 0
palavra = False

for pala in frase:
    if pala != " ":
        if palavra == False:
            somapalavra += 1
            palavra = True
    else:
        palavra = False

print(f'A quantidade de palavras informadas foi: {somapalavra}')