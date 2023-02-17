class Node:
    """ Это узел """

    def __init__(self, data, next_node):
        self.data = data  # тут данные
        self.next_node = next_node  # тут ссылка на следующий


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data, next_node):
        """ Тут добавление элемента """
        new_node = Node(data, next_node)
        new_node.next_node = self.top
        self.top = new_node

