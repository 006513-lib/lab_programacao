def celsius_to_farenheit(celsius):
    farenheit = (celsius * 1.8) + 32
    return farenheit

print("------ Conversor de Temperatura -------")
c = float(input("Digite a temperatura em C.: "))
print(f"A temperatura correspondente é: {celsius_to_farenheit(c)}")