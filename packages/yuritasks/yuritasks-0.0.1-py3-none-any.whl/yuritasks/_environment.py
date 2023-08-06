import os

from typing import Callable


class Task:

    def __init__(self, callback: Callable, subtask: bool) -> None:
        self.namespace: str = callback.__name__.split('_')[0]
        self.name: str = callback.__name__.replace(f"{self.namespace}_", "")
        self.callback: Callable = callback
        self.help: str = "There is no help for this task :("
        self.subtask: bool = subtask
        self.id: int = 0

        if callback.__doc__:
            self.help = callback.__doc__
        
    def set_id(self, id: int) -> None:
        self.id = id


class Environment:

    def __init__(self) -> None:
        self._namespaces: dict = {}
        self.homepath: str = os.getcwd()
    
    def _namespace_init(self, namespace: str) -> None:
        if namespace in self._namespaces.keys():
            return
        
        self._namespaces[namespace] = []
    
    def is_valid_namespace(self, namespace: str) -> bool:
        return namespace in self._namespaces.keys()

    def is_valid_namespace_id(self, namespace_id: int) -> bool:
        return namespace_id < len(self._namespaces.keys())
    
    def is_valid_task_id(self, namespace: str, task_id: int) -> bool:
        return task_id < len(self._namespaces[namespace])
    
    def get_namespace_id(self, namespace: str) -> int:
        return list(self._namespaces.keys()).index(namespace)
    
    def get_namespace_name(self, namespace_id: int) -> str:
        return list(self._namespaces.keys())[namespace_id]
    
    def get_namespaces(self) -> list:
        return self._namespaces.keys()
    
    def get_tasks(self, namespace: str) -> list:
        return self._namespaces[namespace]
    
    def get_task(self, namespace: str, task_id: int) -> Task:
        for task in self._namespaces[namespace]:
            if task.id == task_id:
                return task
    
    def add_task(self, task: Task):
        self._namespace_init(task.namespace)

        task.id = len(self._namespaces[task.namespace])

        self._namespaces[task.namespace].append(task)
