# Exercício Time de Futebol
def registrar_escalacao():
    escalação = []
    print("Digite a escalação dos 11 jogadores titulares (nome e número da camisa):")

    for i in range(11):
        nome = input(f"Jogador {i + 1} - Nome: ")
        numero = input(f"Jogador {i + 1} - Número da camisa: ")
        escalação.append({'nome': nome, 'numero': numero})

    return escalação

def imprimir_escalacao(escalação):
    print("\nEscalação atual do time:")
    for jogador in escalação:
        print(f"Nome: {jogador['nome']}, Número: {jogador['numero']}")

def realizar_substituicoes(escalação):
    substituicoes = 0
    while substituicoes < 3:
        print("\nEscolha um jogador para substituir:")
        numero_substituir = input("Número da camisa do jogador a ser substituído: ")    

def realizar_substituicoes(escalação):
    substituicoes = 0
    while substituicoes < 3:
        print("\nEscolha um jogador para substituir:")
        numero_substituir = input("Número da camisa do jogador a ser substituído: ")    

        jogador_substituir = next((j for j in escalação if j['numero'] == numero_substituir), None)

        if jogador_substituir:
            print(f"Jogador substituído: Nome: {jogador_substituir['nome']}, Número: {jogador_substituir['numero']}")
            novo_nome = input("Nome do novo jogador: ")
            novo_numero = input("Número da nova camisa: ")

            jogador_substituir['nome'] = novo_nome
            jogador_substituir['numero'] = novo_numero

            substituicoes += 1
        else:
            print("Número da camisa não encontrado na escalação. Tente novamente.")

        return escalação  

    def main():
        escalação = registrar_escalacao()
        imprimir_escalacao(escalação) 

        print("\nDurante o intervalo, o técnico pode realizar até 3 substituições.")
    escalação = realizar_substituicoes(escalação)

imprimir_escalacao(escalação)

if __name__ == "__main__":
    main()


    