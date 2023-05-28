"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
from src.linked_list import LinkedList
import unittest


class TestLinkedList(unittest.TestCase):

    def test_insert_beginning(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        self.assertEqual(ll.head.data, {'id': 1})
        ll.insert_beginning({'id': 2})
        self.assertEqual(ll.head.data, {'id': 2})

    def test_insert_at_end(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        ll.insert_at_end({'id': 2})
        ll.insert_at_end({'id': 3})
        ll.insert_beginning({'id': 0})
        self.assertEqual(ll.head.data, {'id': 0})

    def test_str(self):
        ll = LinkedList()
        ll.insert_at_end({'id': 2})
        ll.insert_at_end({'id': 3})
        self.assertEqual(str(ll).strip(), "{'id': 2} -> {'id': 3} -> None")

    def test_to_list(self):
        ll = LinkedList()
        ll.insert_at_end({'id': 2})
        ll.insert_at_end({'id': 3})
        ll.insert_beginning({'id': 1})
        self.assertEqual(ll.to_list(), [{'id': 1}, {'id': 2}, {'id': 3}])

    def test_get_data_by_id(self):
        ll = LinkedList()
        ll.insert_at_end({'id': 2})
        ll.insert_at_end({'id': 3})
        ll.insert_beginning({'id': 1})
        self.assertEqual(ll.get_data_by_id(1), {'id': 1})


if __name__ == '__main__':
    unittest.main()
