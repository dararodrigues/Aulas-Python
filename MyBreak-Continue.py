# Demonstração do Uso de Estrutura Repetitiva...
CONTADOR = 0; SENHA = ""
while SENHA != "S3nh4":
    print("Digite a Senha:")
    SENHA = input()

    if SENHA =="S3nh4":
        print("Senha Correta!")
        break
    else:
        print("Senha Errada...")

        CONTADOR = CONTADOR + 1
        if CONTADOR == 3:
            print("Tentativas Excedidas!")
            break