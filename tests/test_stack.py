"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Stack


class TestStack(unittest.TestCase):
    def test_push(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.top.data, 1)
        stack.push('22')
        self.assertEqual(stack.top.next_node.data, 1)

    def test_pop(self):
        stack = Stack()
        stack.push(2)
        stack.push('33')
        stack.pop()
        self.assertEqual(stack.top.data, 2)
        stack.pop()
        self.assertIsNone(stack.top)

    def test_str(self):
        stack = Stack()
        self.assertEqual(stack.__str__(), '')
        stack.push(3)
        self.assertEqual(stack.__str__(), 3)


if __name__ == '__main__':
    unittest.main()
    