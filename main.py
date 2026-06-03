numero = 1
while numero != 0:
    print("")
    try:
        numero = float(input("Insira o número e descubra a tabuada: "))
        for i in range(1,11):
            print(f"A tabuada do {numero} x {i} é: {numero*i:.2f}")
        print("")
    except ValueError:
        print("Insira um valor correto!")
        print("")

#------------------------------------------------------------------

    print("Deseja inserir um número?")
    confirmacao = input("Responda com Y ou N: ").upper()
    if confirmacao == "Y":
        numero = 1
    elif confirmacao == "N":
        numero = 0
        break
    else:
        while confirmacao != "Y" and confirmacao != "N":
            print("Desculpe, não compreendi.")
            print("")
            print("Deseja inserir um número?")
            confirmacao = input("Responda com Y ou N: ").upper()
            if confirmacao == "N":
                break
    if confirmacao == "N":
        break
