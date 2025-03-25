tasks = []

print("Добро пожаловать в to-do list!")
print('Выберите "add" для создания задачи')
print('Выберите "remove" для удаления задачи')
print('Выберите "view" для выведения всех задач')
print('Выберите "complete" чтобы пометить задачу как выполненную')

def add_task():
    description = input("Введите название новой задачи: ")
    new_task = [description, False]
    tasks.append(new_task)
    print("Новая задача успешно добавлена!")

def remove_task():
    if not tasks:
        print("Список задач пуст!")
        return

    view_tasks()
    try:
        index = int(input("Введите номер задачи, которую хотите удалить: "))
        if 1 <= index <= len(tasks):
            removed_task = tasks.pop(index - 1)
            print(f"Задача '{removed_task[0]}' удалена!")
        else:
            print("Ошибка, индекс за пределами списка")
    except ValueError:
        print("Ошибка: Введите число!")

def view_tasks():
    if not tasks:
        print("Список задач пуст!")
        return

    print("\nВаши задачи:")
    for i, task in enumerate(tasks, start=1):
        status = "Выполнено" if task[1] else "Не выполнено"
        print(f"{i}. {task[0]} - {status}")

def mark_task_completed():
    if not tasks:
        print("Список задач пуст!")
        return

    view_tasks()
    try:
        mark_task_index = int(input("Введите номер задачи, которую хотите отметить как выполненную: "))
        if 1 <= mark_task_index <= len(tasks):
            tasks[mark_task_index - 1][1] = True 
            print(f"Задача '{tasks[mark_task_index - 1][0]}' отмечена как выполненная!")
        else:
            print("Ошибка, индекс за пределами списка")
    except ValueError:
        print("Ошибка: Введите число!")

def to_do_list():
    while True:
        choice = input("\nВведите операцию: ").strip().lower()
        if choice == "add":
            add_task()
        elif choice == "remove":
            remove_task()
        elif choice == "view":
            view_tasks()
        elif choice == "complete":
            mark_task_completed()
        else:
            print("Ошибка, введите правильную команду!")

        next_operation = input("Хотите ли Вы проводить еще операции? (yes/no): ").strip().lower()
        if next_operation != "yes":
            print("Спасибо за использование!")
            break

to_do_list()