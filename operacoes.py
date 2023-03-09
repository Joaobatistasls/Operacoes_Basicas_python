import somar
import subtracao
import multiplicacao
import divisao

print("**** Operações Matemáticas ****")

print("(1) Adição (2) Subtração (3) Multiplicação (4) Divisão")

operacao = int(input("Qual operação matemática deseja usar?"))

if (operacao == 1):
    print("Usando a Adição")
    somar.somar_numero()
elif (operacao == 2):
    print("Usando a Subtração")
    subtracao.subtrair_numero()
elif (operacao == 3):
    print("Usando a Multiplicação")
    multiplicacao.multiplicar_numero()
elif (operacao == 4):
    print("Usando a Divisão")
    divisao.dividir_numero()
