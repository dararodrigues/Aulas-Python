# Demonstração do Comportamento de Listas....
print("Vou Almoçar wm um Restaurante a quilo!")

ORIGINAL = ["arroz", "feijão", "batata", "alface", "frango"]
print("Eis, a Minha Comida:", ORIGINAL)
DERIVADA = ORIGINAL
print("Meu amigo irá comer Tambem:", DERIVADA)

print("Vou Alterar as Opções sem ele ver...")
ORIGINAL.remove("arroz")
ORIGINAL.remove("feijão")
ORIGINAL.remove("alface")
ORIGINAL.append("picanha")
ORIGINAL.append("linguiça")

print("Amiguinho me Mostre o que Você vai Comer?")
print("Claro! Dá uma Conferida", DERIVADA)