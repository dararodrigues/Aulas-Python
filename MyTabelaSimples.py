# Demonstraçã de Mattrizes Simples em Python...
print("Eis a Tabela Numérica Original")
Tabuada = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9,]]
Multiplicar= int(input("Digite o Multiplicador:" ))

for x in range(0, 3):
    for y in range(0, 3):
        Tabuada[x][y] = Tabuada[x][y] * Multiplicar

print("Eis, o Multiplicador:", Multiplicar)
print("Confira o Resultado das Operações")
for Resultado in Tabuada:
    print(Resultado)
    