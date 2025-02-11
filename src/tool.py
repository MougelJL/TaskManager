import argparse
import os

class CLI ():

    def __init__(self):
        self.cwd = os.getcwd() #Current Working Directory
        self.tasks_file_path = ... #Path where the tasks.json file is located
        self.history_path = ... #Path where the history of previous actions is located
        self.tasks_file = ...
        self.history_file = ...

    def add_task (self, task_name:str) -> None:
        pass

    def delete_task (self, task_id: int) -> None:
        pass
    
    def list_tasks (self, status: str) -> str:
        pass

    def update_task (self, task_id: int, new_task_name: str) -> None:
        pass