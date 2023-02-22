class Node:

    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data, next_node):
        new_node = Node(data, next_node)
        new_node.next_node = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        else:
            temp = self.top
            self.top = self.top.next_node
            return temp.data
