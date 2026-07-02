entrada = input('digite uma palavra para teste: ').lower()
novapala = ''

for i in entrada:
    if i == 'a':
        novapala +='*'
    else:
        novapala += i

print(novapala)