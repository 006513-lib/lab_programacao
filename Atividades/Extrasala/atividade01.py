while True:
    num = int(input('digite um numero para teste (0 para sair): '))
    if 10 < num < 50:
        print('Perfeito. Dado válido!')
    if num == 0:
        break
    else:
        print('Desculpe. Dado inválido.')
