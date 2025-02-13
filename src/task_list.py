from task import Task
from task_status import TaskStatus

class Tasklist:
    def __init__(self, task: Task, child: 'Tasklist' = None, parent: 'Tasklist' = None) -> None:
        self.task: Task = task
        self.id: int = 0

        #This makes the root node parent of itself
        if parent is not None:
            self.parent_node = parent
        else:
            self.parent_node = self
        
        #This makes the root node child of itself
        if child is not None:
            self.child_node = child
        else:
            self.child_node = self

    
    def add_task (self, task: Task, root_node: 'Tasklist' = None) -> None:

        if self.child_node == root_node:
            task_node = Tasklist(task, root_node, self)
            

        else:
            self.child_node.add_task(task, root_node)
