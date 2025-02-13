import datetime
from .task_status import TaskStatus

class Task:
    def __init__(self, name: str = None, status = TaskStatus.TO_DO) -> None:
                 
        #Data and meta
        self.Id: int = None
        self.name: str = name
        self.status: TaskStatus = status       
        self.creation_date: datetime.date = ...
        self.update_date: datetime.date = ...
        
    def __str__(self):
        return f'Name: {self.name}\nStatus: {self.status.value}'    

    #Getters and setters
    @property
    def Id(self) -> int:
        return self._Id
    
    @Id.setter
    def Id(self, value:int) -> None:
        self._Id = value

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

    @property
    def creation_date(self) -> datetime.date:
        return self._creation_date

    @creation_date.setter
    def creation_date(self, value: datetime.date) -> None:
        self._creation_date = value

    @property
    def update_date(self) -> datetime.date:
        return self._update_date

    @update_date.setter
    def update_date(self, value: datetime.date) -> None:
        self._update_date = value

    @property
    def parent_task(self) -> 'Task':
        return self._parent_task

    @parent_task.setter
    def parent_task(self, value: 'Task') -> None:
        self._parent_task = value

    @property
    def children_task(self) -> 'Task':
        return self._children_task

    @children_task.setter
    def children_task(self, value: 'Task') -> None:
        self._children_task = value

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, value: int) -> None:
        self._id = value
