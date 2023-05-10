"""Здесь надо написать тесты с использованием unittest для модуля queue."""
from src.queue import Queue
import unittest


class TestQueue(unittest.TestCase):

    def test_enqueue(self):
        queue = Queue()
        self.assertIsNone(queue.head)
        queue.enqueue('test')
        self.assertEqual(queue.tail.data, 'test')
        queue.enqueue('test1')
        queue.enqueue('test2')
        self.assertEqual(queue.head.data, 'test')
        self.assertEqual(queue.head.next_node.data, 'test1')
        self.assertEqual(queue.tail.data, 'test2')

    def test_str(self):
        queue = Queue()
        queue.enqueue(1)
        self.assertEqual(queue.__str__(), '1')
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(queue.__str__(), '1\n2\n3')


if __name__ == '__main__':
    unittest.main()
