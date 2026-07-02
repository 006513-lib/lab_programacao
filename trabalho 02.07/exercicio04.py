frase = input('Digite qualquer frase: ').lower()

palavra = ''
fraseinv = ''

for i in range(len(frase) -1,-1,-1):
    if frase[i] != ' ':
        palavra = frase[i] + palavra 
    else:
        fraseinv += palavra + ' '
        palavra = ''

fraseinv += palavra

print(fraseinv)