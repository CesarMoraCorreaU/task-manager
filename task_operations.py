from models import Task, TaskList

from models import Task, TaskList

def create_task(task_list, description):
    """
    Crea una nueva tarea y la añade a la lista
    Args:
        task_list: Objeto TaskList
        description: Descripción de la tarea
    Returns:
        Task: La tarea creada
    """
    new_task = Task(description)
    task_list.add_task(new_task)
    return new_task