from django.test import TestCase
from .models import Todo

class TodoTestCase(TestCase):
    def setUp(self):
        # Create some initial Todo objects for testing
        self.todo1 = Todo.objects.create(
            todo_title="Test Todo 1",
            todo_description="Description for Test Todo 1",
            is_done=False
        )
        self.todo2 = Todo.objects.create(
            todo_title="Test Todo 2",
            todo_description="Description for Test Todo 2",
            is_done=True
        )

    def test_todo_str_method(self):
        # Test the __str__ method of the Todo model
        self.assertEqual(str(self.todo1), "Test Todo 1")
        self.assertEqual(str(self.todo2), "Test Todo 2")

    def test_todo_properties(self):
        # Test properties or methods of the Todo model as needed
        self.assertEqual(self.todo1.is_done, False)
        self.assertEqual(self.todo2.is_done, True)

    # Add more test methods as needed
