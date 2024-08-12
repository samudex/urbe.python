tasks = []


def create_task(task_id, title, description, status):
    if any(task["id"] == task_id for task in tasks):
        print(f"Error: El ID '{task_id}' ya está registrado.")
        return
    task = {"id": task_id, "title": title, "description": description, "status": status}
    tasks.append(task)
    print(f"Tarea '{title}' creada con ID: {task_id}")


def modify_task(task_id, title=None, description=None, status=None):
    for task in tasks:
        if task["id"] == task_id:
            if title:
                task["title"] = title
            if description:
                task["description"] = description
            if status is not None:
                task["status"] = status
            print(f"Tarea '{task_id}' modificada.")
            return
    print(f"Tarea con ID '{task_id}' no encontrada.")


def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    print(f"Tarea con ID '{task_id}' eliminada.")


def search_task(keyword):
    results = filter(
        lambda task: keyword.lower() in task["title"].lower()
        or keyword.lower() in task["description"].lower(),
        tasks,
    )
    for task in results:
        print(
            f"ID: {task['id']}, Título: {task['title']}, Descripción: {task['description']}, Estatus: {'Completada' if task['status'] else 'Pendiente'}"
        )


def filter_tasks(status):
    results = [task for task in tasks if task["status"] == status]
    for task in results:
        print(
            f"ID: {task['id']}, Título: {task['title']}, Descripción: {task['description']}, Estatus: {'Completada' if task['status'] else 'Pendiente'}"
        )


def list_tasks():
    for task in tasks:
        print(
            f"ID: {task['id']}, Título: {task['title']}, Descripción: {task['description']}, Estatus: {'Completada' if task['status'] else 'Pendiente'}"
        )


def main():
    while True:
        print("\nOpciones:")
        print("1. Crear tarea")
        print("2. Modificar tarea")
        print("3. Eliminar tarea")
        print("4. Buscar tarea")
        print("5. Filtrar tareas")
        print("6. Listar todas las tareas")
        print("7. Salir")

        choice = input("Selecciona una opción: ")

        match choice:
            case "1":
                task_id = int(input("ID: "))
                title = input("Título: ")
                description = input("Descripción: ")
                status = (
                    input(
                        "Estatus (True para completada, False para pendiente): "
                    ).lower()
                    == "true"
                )
                create_task(task_id, title, description, status)
            case "2":
                task_id = int(input("ID de la tarea a modificar: "))
                title = input("Nuevo título (dejar en blanco para no cambiar): ")
                description = input(
                    "Nueva descripción (dejar en blanco para no cambiar): "
                )
                status_input = input(
                    "Nuevo estatus (True para completada, False para pendiente, dejar en blanco para no cambiar): "
                ).lower()
                status = None if status_input == "" else status_input == "true"
                modify_task(task_id, title, description, status)
            case "3":
                task_id = int(input("ID de la tarea a eliminar: "))
                delete_task(task_id)
            case "4":
                keyword = input("Palabra clave para buscar: ")
                search_task(keyword)
            case "5":
                status = (
                    input(
                        "Estatus para filtrar (True para completada, False para pendiente): "
                    ).lower()
                    == "true"
                )
                filter_tasks(status)
            case "6":
                list_tasks()
            case "7":
                break
            case _:
                print("Opción no válida. Inténtalo de nuevo.")


if __name__ == "__main__":
    main()
