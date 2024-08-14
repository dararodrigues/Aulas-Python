# Demonstração de Funções em Listas....
print("Eis, os Meus Maiores Sonhos....")
SONHOS = ["1. Me Divertir na Disney",
          "2. Me banhar na Praia de Sepetiba",
          "Tirar Férias em Paris,"
          "4. Fazer Compras no WestShopping",
          "5. Ver As Pirâmides do Egito"]
for x in SONHOS:
    print(x)

print("Ops, Não Quero Sepetiba!")
del(SONHOS[1])
print("E Nem WestShopping...")
del(SONHOS[2])

print("Conferindo os Sonhos....")
for x in SONHOS:
    print(x)
