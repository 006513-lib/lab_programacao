def permitir_acesso(nascimento):
    idade =  2026 - nascimento
    if idade >= 18:
        return True
    else:
        return False
    
print("---- Validador de Sistemas ----")
ano = int(input("Em qual ano tu nasceu, caboco? "))
if permitir_acesso(ano):
    print("Acesso liberado! :)")
else:
    print("Acesso Bloqueado")