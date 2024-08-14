# Demonstração do Uso de Funções....
def APRESENTAR():
    print("Meu Nome é",MyName,",")
    print("Minha Altura é de",MyHeigh,"Metros")
    print("Minha Idade é",MyAge,"Anos")
    return

def CONFERIR(x):
    if x >= 18:
        print("Voçê é Maior de Idade!")
    else:
        print("Ops, Menor de Idade Não Pode!")    
    return

MyName = str(input("Digite o Seu Nome:"))  
MyHeigh = float(input("Digite a Sua Altura:"))
MyAge = int(input("Digite a Sua Idade:")) 

APRESENTAR()
CONFERIR(MyAge)
