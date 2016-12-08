import unittest
from stack import Stack

class StackTest(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_if_new_stack_is_empty(self):
        self.assertTrue(self.stack.isEmpty())
        self.stack.push(1)
        self.assertFalse(self.stack.isEmpty())

    def test_stack_push(self):
        self.stack.push(2)
        self.assertEqual(self.stack.peek(), 2)
        self.assertEqual(self.stack.size(), 1)

    def test_stack_pop(self):
        self.stack.push(3)
        self.stack.pop()
        self.assertEqual(self.stack.size(), 0)

    def test_stack_peek(self):
        self.stack.push(4)
        self.assertEqual(self.stack.peek(), 4)

    def test_stack_size(self):
        self.stack.push(5)
        self.stack.push(6)
        self.assertEqual(self.stack.size(), 2)