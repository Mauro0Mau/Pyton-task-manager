import os
from InquirerPy import prompt
from rich import print

tasks_path = os.path.join(os.path.dirname(__file__), "tarefas.txt")


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def voltar_menu():
    input("\nPressione Enter para voltar ao menu...")


while True:
    limpar_tela()

    questions = [
        {
            "type": "list",
            "name": "opcao",
            "message": "Escolha uma opção:",
            "choices": [
                {"name": "1. Criar tarefa", "value": 1},
                {"name": "2. Listar tarefas", "value": 2},
                {"name": "3. Concluir tarefa", "value": 3},
                {"name": "4. Sair", "value": 4},
            ],
        }
    ]

    opcao = prompt(questions)["opcao"]

    if opcao == 1:
        titulo = input("Digite o título da tarefa: ")

        with open(tasks_path, "a", encoding="utf-8") as arquivo:
            arquivo.write(f"[ ] {titulo}\n")

        print("[green]Tarefa criada com sucesso![/green]")
        voltar_menu()

    elif opcao == 2:
        if os.path.exists(tasks_path):
            with open(tasks_path, "r", encoding="utf-8") as arquivo:
                tarefas = arquivo.readlines()

            print("\n[cyan]Lista de tarefas:[/cyan]")

            if tarefas:
                for i, tarefa in enumerate(tarefas, start=1):
                    print(f"{i}. {tarefa.strip()}")
            else:
                print("[yellow]Nenhuma tarefa cadastrada.[/yellow]")
        else:
            print("[yellow]Nenhuma tarefa cadastrada.[/yellow]")

        voltar_menu()

    elif opcao == 3:
        if os.path.exists(tasks_path):
            with open(tasks_path, "r", encoding="utf-8") as arquivo:
                tarefas = arquivo.readlines()

            if tarefas:
                print("\n[cyan]Lista de tarefas:[/cyan]")

                for i, tarefa in enumerate(tarefas, start=1):
                    print(f"{i}. {tarefa.strip()}")

                try:
                    indice = int(
                        input("\nDigite o número da tarefa concluída: ")
                    ) - 1

                    if 0 <= indice < len(tarefas):
                        tarefas[indice] = tarefas[indice].replace(
                            "[ ]", "[X]", 1
                        )

                        with open(tasks_path, "w", encoding="utf-8") as arquivo:
                            arquivo.writelines(tarefas)

                        print("[green]Tarefa concluída![/green]")
                    else:
                        print("[red]Número inválido.[/red]")

                except ValueError:
                    print("[red]Digite apenas números.[/red]")
            else:
                print("[yellow]Nenhuma tarefa cadastrada.[/yellow]")
        else:
            print("[yellow]Nenhuma tarefa cadastrada.[/yellow]")

        voltar_menu()

    elif opcao == 4:
        print("[blue]Encerrando programa...[/blue]")
        break