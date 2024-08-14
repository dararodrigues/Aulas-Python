# Exercício GABARITOS PROVA
GABARITO = ['B', 'C', 'A', 'E', 'D']

def verificar_acertos(respostas_usuario):
    acertos = 0

    for i in range(len(GABARITO)):
        if respostas_usuario[i].upper() == GABARITO[i]:
            acertos += 1
        return acertos

def main():
     print("Por favor, insira suas respostas para as 5 questões da prova:")
    
respostas_usuario = []
for i in range(5):
        resposta = input(f"Resposta para a questão {i + 1} (A, B, C, D ou E): ").strip().upper()
        respostas_usuario.append(resposta)

acertos = verificar_acertos(respostas_usuario)

print(f"Você acertou {acertos} de 5 questões.")

if __name__ == "__main__":
 main()
