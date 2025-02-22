import datetime
from .task_status import TaskStatus

"""
NOTE: Date and time in task features are yet to be implemented, the comments are just placeholders
NOTE: ID was removed from the class
"""
class Task:
    def __init__(self, name: str = None, status = TaskStatus.TO_DO) -> None:
                 
        #self.id: int = None
        self.name: str = name
        self.status: TaskStatus = status   

        
    def __str__(self):
        return f'Name: {self.name}\nStatus: {self.status.value}\nID: {self.id}'    

    def __eq__(self, other: 'Task') -> bool:
        return self.name == other.name and self.status == other.status
    
    def is_empty (self) -> bool:
        return self.name == None or self.name == ""
         

    #Getters and setters
    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @property
    def status(self) -> TaskStatus:
        return self._status

    @status.setter
    def status(self, value: str) -> None:
        self._status = value
