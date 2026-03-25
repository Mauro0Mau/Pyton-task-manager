
while True:
    # Menu
    print("┌───── Menu Calculadora ─────┐")
    print("│                            │")
    print("│   Escolha uma opção !      │")
    print("│      1 - Soma              │")
    print("│      2 - Subtração         │")
    print("│      3 - Multiplicar       │")
    print("│      4 - Divisão           │")
    print("│             ☻              │")
    print("│                            │")
    print("└─────────────//─────────────┘\n")

    opcao = int(input("Opção: "))
    
    quantidade = int(input("Quantas variaveis deseja somar? (Minimo 2):"))

    if opcao == 1:
        print("Soma selecionada!")
    elif opcao == 2:
        print("Subtração selecionada!")
    elif opcao == 3:
        print("Multiplicação selecionada!")
    elif opcao == 4:
        print("Divisão selecionada!")
    else:
        print("Número inválido! Digite de 1 a 4.")

    num1 = float(input("Primeiro numero: "))
    num2 = float(input("Segundo numero: "))

    if opcao == 1:
        resultado = num1 + num2
    elif opcao == 2:
        resultado = num1 - num2
    elif opcao == 3:
        resultado = num1 * num2
    elif opcao == 4:
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("ERRO: Divisão por 0 não permitida!")
            resultado = 0  # or handle differently, but in C it's not set
    else:
        resultado = 0  # for invalid, maybe not print

    print("╔════ Resultado: ════╗")
    print(f"  {resultado:.2f}")
    print("╚════════════════════╝")

    continuar = input("Deseja continuar? (s/n): ").strip().lower()
    if continuar != 's':
        break

print("Programa finalizado. Adeus")
