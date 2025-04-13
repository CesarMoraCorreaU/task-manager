import uuid

class Task:
    """Clase que representa una tarea en el sistema"""
    
    def __init__(self, description):
        self.id = str(uuid.uuid4())
        self.description = description
        self.completed = False
    
    def to_dict(self):
        """Convierte el objeto Task a un diccionario"""
        return {
            'id': self.id,
            'description': self.description,
            'completed': self.completed
        }

class TaskList:
    """Clase que maneja la colección de tareas"""
    
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        """Añade una tarea a la lista"""
        self.tasks.append(task)
    
    def get_all_tasks(self):
        """Obtiene todas las tareas"""
        return self.tasks
    
    def find_task_by_id(self, task_id):
        """Busca una tarea por su ID"""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None