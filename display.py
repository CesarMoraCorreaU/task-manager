from models import TaskList

def show_all_tasks(task_list):
    """
    Muestra todas las tareas en formato legible
    Args:
        task_list: Objeto TaskList
    """
    if not task_list.get_all_tasks():
        print("No hay tareas disponibles.")
        return
    
    print("\n--- Lista de Tareas ---")
    for i, task in enumerate(task_list.get_all_tasks(), 1):
        status = "✓" if task.completed else "✗"
        print(f"{i}. [{status}] {task.description} (ID: {task.id})")

def show_task_details(task):
    """
    Muestra los detalles de una tarea específica
    Args:
        task: Objeto Task
    """
    print("\n--- Detalles de Tarea ---")
    print(f"ID: {task.id}")
    print(f"Descripción: {task.description}")
    print(f"Estado: {'Completada' if task.completed else 'Pendiente'}")

def show_menu():
    """Muestra el menú principal"""
    print("\n--- Menú Principal ---")
    print("1. Añadir nueva tarea")
    print("2. Ver todas las tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")