"""
Faça uma lista de tarefas com as seguintes opções:
    - Adicionar uma tarefa
    - Listar tarefas
    - Opção de desfazer (a5 cada vez que chamarmos, desfaz a última ação)
    - Opção de refazer (a cada vez que chamarmos. refaz a última ação)
"""


def show_op(todo_list):
    print()
    print("Tarefas: ")
    print(todo_list)
    print()


def do_undo(todo_list, redo_list):
    if not todo_list:
        print("Nada a desfazer")
        return

    last_todo = todo_list.pop()
    redo_list.append(last_todo)


def do_redo(todo_list, redo_list):
    if not redo_list:
        print("Nada a refazer")
        return

    last_redo = redo_list.pop()
    todo_list.append(last_redo)


def do_add(todo, todo_list):
    todo_list.append(todo)


if __name__ == "__main__":
    todo_list = []
    redo_list = []

    while True:
        todo = input("Digite uma tarefa ou ls,undo, redo: ")

        if todo == "ls":
            show_op(todo_list)
            continue
        elif todo == "undo":
            do_undo(todo_list, redo_list)
            continue
        elif todo == "redo":
            do_redo(todo_list, redo_list)
            continue

        do_add(todo, todo_list)
