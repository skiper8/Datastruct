import unittest
from utils.utils import *


class TestNode(unittest.TestCase):
    def test_node(self):
        node = Node(1, None)
        self.assertEqual(node.data, 1)
        self.assertEqual(node.next_node, None)

    def test_node_next_node(self):
        node1 = Node(1, None)
        node2 = Node(2, node1)
        self.assertEqual(node2.next_node, node1)
        self.assertEqual(node2.next_node.data, 1)


class TestStack(unittest.TestCase):
    def test_stack_push(self):
        stack = Stack()
        stack.push('data_2', None)
        stack.push('data_1', None)
        self.assertEqual(stack.top.data, 'data_1')
        self.assertEqual(stack.top.next_node.data, 'data_2')

    def test_stack_pop(self):
        stack = Stack()
        stack.push('data_1', None)
        self.assertEqual(stack.pop(), "data_1")
