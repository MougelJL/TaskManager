from dataclasses import dataclass
from enum import Enum


@dataclass 
class TaskStatus(Enum):
    """Class for status types for tasks"""
    DOING = "Doing"
    TO_DO = "To do"
    DONE = "Done"