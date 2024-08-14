# Demonstração do Uso de funções ....
def ADICAO(x,y):
    return x + y
def SUBTRACAO(x,y):
    return x - y
def MULTIPLICACAO(x,y):
    return x * y
def DIVISAO(x,y):
    return x / y

print("Digite Dois Valores Inteiros....")
N1 = int(input("x:"))
N2 = int(input("y:"))
OP = input("Qual Operação (+ ou - )?")

if OP == "+":
   z = ADICAO(N1,N2)
   print("Resultado da Soma:", z)

elif OP == "-":
    z = SUBTRACAO(N1,N2)
    print("Resultado da Subtração:", z)
else:
    print("Opção Digitada Inexistente!")

