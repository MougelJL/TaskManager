import unittest
from .. import Task

class TaskTestCase(unittest.TestCase):

    def setUp(self):
        self.task = Task("Clean the dishes")

    def test_task_set_id(self):
        self.task.id = 1
        self.assertEqual(self.task.id, 1)