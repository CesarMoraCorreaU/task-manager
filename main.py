from models import TaskList
from task_operations import create_task
from display import show_menu

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
        
        elif choice == "5":
            print("\n¡Hasta luego!")
            break
        
        else:
            print("\nOpción no válida. Por favor intente de nuevo.")

if __name__ == "__main__":
    main()