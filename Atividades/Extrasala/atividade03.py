palavra = input('digite qualquer palavra: ').lower()

vogais=0
for letra in palavra:
    if letra in 'a''e''i''o''u':
        vogais+=1
print(f'o número de vogais encontradas na palavra {palavra} foi de {vogais}')