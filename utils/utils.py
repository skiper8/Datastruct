class Node:

    def __init__(self, data, next_node):
        self.data = data  # тут данные
        self.next_node = next_node  # тут ссылка на следующий


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


stack = Stack()
stack.push('data1', None)
data = stack.pop()

# стэк стал пустой
print(stack.top)

print(data)
'data1'


stack = Stack()
stack.push('data1', None)
stack.push('data2', None)
data = stack.pop()
print(stack.top.data)

print(data)
