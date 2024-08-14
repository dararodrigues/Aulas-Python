# DEmonstraçaõ de Matrizes Em Python...
print("Eis, o teclado numérico do terminal:")
Teclado = [["1", "2", "3",],
           ["4", "5", "6"],
           ["7", "8", "9"],
           ["0", "#", "*"]]

Senha = []

print("Digite a sua Senha de 4 Digitos...")
for x in range(0, 4):
    Senha.append(input(f'Digite o Digito{x+1}:'))

for x in range(0, 4):
    for y in range(0, 3):
        for z in range(0, 4):
            if Teclado[x][y] == Senha[z]:    
                Teclado[x][y] = "X"

print("Eis, a Senha Digitada:", Senha)  
print("Confira, as Teclas Acionadas:")
for Listas in Teclado:
    print(Listas)                    