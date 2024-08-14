# Exercício Lista de Tarefas....

def exibir_tarefas(tarefas):
    """Exibe a lista de tarefas com numeração."""
    print("\nLista de Tarefas:")
    for i, tarefa in enumerate(tarefas, start=1):
        print(f"{i}. {tarefa}")

def adicionar_tarefa(tarefas):
    """Adiciona uma nova tarefa à lista, se houver espaço."""
    if len(tarefas) < 5:
        nova_tarefa = input("Digite a nova tarefa: ")
        tarefas.append(nova_tarefa)
    else:
        print("A lista já está cheia. Exclua uma tarefa antes de adicionar uma nova.")

def remover_tarefa(tarefas, indice):
    """Remove a tarefa da lista com base no índice fornecido."""
    if 0 <= indice < len(tarefas):
        tarefas.pop(indice)
    else:
        print("Índice inválido.") 

def main():
    tarefas = []   

    while len(tarefas) < 5:
        tarefa = input(f"Digite a tarefa {len(tarefas) + 1} (ou digite 'fim' para terminar): ")
        if tarefa.lower() == 'fim':
            break
        tarefas.append(tarefa)

    exibir_tarefas(tarefas)   

    if tarefas:
        resposta = input(f"A primeira tarefa '{tarefas[0]}' foi executada? (s/n): ").strip().lower()
        if resposta == 's':
            remover_tarefa(tarefas, 0)
            print("Tarefa removida.")
            exibir_tarefas(tarefas) 

            adicionar_tarefa(tarefas)
            print("Nova tarefa adicionada.")
            exibir_tarefas(tarefas)
        elif resposta == 'n':
            print("A tarefa não foi removida.")
        else:
            print("Resposta inválida.")
    else:
        print("A lista de tarefas está vazia.")
     