# Demonstração de matrizes em Python....
Tabuada = []

for x in range (0,10):
    Linhas = []
    for y in range(0,10):
        Linhas.append(x*y)
    Tabuada.append(Linhas)   


for Tabela in Tabuada:
    print(Tabela)