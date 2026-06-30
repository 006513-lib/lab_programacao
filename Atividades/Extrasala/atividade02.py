num = int(input('digite um numero (inteiro e positivo): '))

lista = []
produto = 1

for i in range(1,num+1,2):
    lista.append(i)
    produto *= i
print(lista)
print(f'o produto obtido dos números {num} é: {produto}')
    