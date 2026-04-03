

def mostrar_menu():
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Concluir tarefa")
    print("4. Sair")

def adicionar_tarefa():
    pass

def listar_tarefas():
    pass

def concluir_tarefa():
    pass

def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha: ")

        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            concluir_tarefa()
        elif opcao == "4":
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()








