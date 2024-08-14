# demonstração de Acesso a Lista...

print("Vou Montar a Lista Com 5 Alimentos!")
MARMITA = {"feijão", "arroz", "legumes", "salada", "carne"}
print("Eis a Nossa recomendação:", MARMITA)

RESPOSTA = input("Voçê quer Montar uma Marmita Diferente(S/N)?")
if RESPOSTA == "S":
    for x in range(0, 5):
        print(f'Digite o {x+1}o. item do Cardápio:')
        MARMITA[x] = input()
    print("A Marmita Montada Foi:, MARMITA")
    print("Os Tres Primeiros Itens Foram:", MARMITA[0:3])
    print("O Último Item da Marmita foi:", MARMITA[-1])
else:
    print("OK. VoÇê Decide...")


