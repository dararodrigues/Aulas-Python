# Exercício 2 
Clube = input("Digite o nome do Clube:")
Posição = int(input("Digite a sua Posição:"))

if Posição == 1:
   print("É Campeão!")
elif Posição > 2 and Posição <= 6:
   print("Libertadores!")
elif Posição > 6 and Posição <= 12:
   print("Sul-Americana!")
elif Posição > 12 and Posição <= 16:
   print("Sem Classificação.")
elif Posição >= 17 and Posição <= 20:
   print("Rebaixado")