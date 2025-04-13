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

def list_all_tasks(task_list):
    """
    Obtiene todas las tareas de la lista
    Args:
        task_list: Objeto TaskList
    Returns:
        list: Lista de todas las tareas
    """
    return task_list.get_all_tasks()

def mark_task_completed(task_list, task_id):
    """
    Marca una tarea como completada
    Args:
        task_list: Objeto TaskList
        task_id: ID de la tarea
    Returns:
        tuple: (Task|None, error_message|None)
    """
    task = task_list.find_task_by_id(task_id)
    if task:
        task.completed = True
        return task, None
    return None, "Task not found"

def delete_task(task_list, task_id):
    """
    Elimina una tarea de la lista
    Args:
        task_list: Objeto TaskList
        task_id: ID de la tarea
    Returns:
        tuple: (bool, error_message|None)
    """
    task = task_list.find_task_by_id(task_id)
    if task:
        task_list.tasks.remove(task)
        return True, None
    return False, "Task not found"