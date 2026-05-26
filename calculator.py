import os
sentinela = 1

while(sentinela == 1):
    print("*********************************")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("*********************************")

    operacao = input("Escolha a operação: ")
    valor1 = input("Digite o primeiro número: ")
    valor2 = input("Digite o segundo número: ")

    operacao = int(operacao)
    valor1 = float(valor1)
    valor2 = float(valor2)

    if(operacao == 1):
        resultado = valor1+valor2
    elif(operacao == 2):
        resultado = valor1-valor2
    elif(operacao == 3):
        resultado = valor1*valor2
    elif(operacao == 4):
        resultado = valor1/valor2
    else:
        resultado = 0
        print("Escolhe o bagui certo prç")

    print("Resultado: ", resultado)

    print("-------------------------------------")
    print("Deseja continuar?")
    print("1 - Sim")
    print("2 - Não")
    sentinela = input("Informe a opção: ")
    sentinela = int(sentinela)
    os.system("cls")