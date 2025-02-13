#import argparse
import os

class Cli ():

    def __init__(self):
        self.cwd = os.getcwd() #Current Working Directory
        self.tasks_file_path = ... #Path where the tasks.json file is located
        self.history_path = ... #Path where the history of previous actions is located
        self.tasks_file = ...
        self.history_file = ...

    def add_task (self, task_name:str) -> None:
        """Creates and adds a new Task Object to a to an already existing Tasklist Object
        """
        pass

    def delete_task (self, task_id: int = None, task_name: str = None) -> None:
        """Removes a task from a Tasklist Object using either their name or ID

        task_id (integer)
        """
        pass
    
    def list_tasks (self, status: str) -> str:
        pass

    def update_task (self, task_id: int, new_task_name: str) -> None:
        pass