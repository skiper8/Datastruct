class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.head is None:
            return None
        dequeue_element = self.head
        self.head = self.head.next
        return dequeue_element.data


queue = Queue()
queue.enqueue('data1')
queue.enqueue('data2')
queue.enqueue('data3')
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
