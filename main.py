from models import TaskList
from task_operations import create_task, mark_task_completed
from display import show_menu, show_all_tasks, show_task_details

def main():
    """Función principal del programa: solo permite crear tareas"""
    task_list = TaskList()
    
    while True:
        show_menu()
        choice = input("Seleccione una opción (1-5): ")
        
        if choice == "1":
            description = input("Ingrese la descripción de la tarea: ")
            task = create_task(task_list, description)
            print(f"\nTarea creada con ID: {task.id}")
        
        elif choice == "2":
            show_all_tasks(task_list)
        
        elif choice == "3":
            show_all_tasks(task_list)
            task_id = input("\nIngrese el ID de la tarea a completar: ")
            task, error = mark_task_completed(task_list, task_id)
            if error:
                print(f"\nError: {error}")
            else:
                print("\nTarea marcada como completada:")
                show_task_details(task)
        
        elif choice == "5":
            print("\n¡Hasta luego!")
            break
        
        else:
            print("\nOpción no válida. Por favor intente de nuevo.")

if __name__ == "__main__":
    main()