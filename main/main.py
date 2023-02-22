from utils.utils import *

stack = Stack()
stack.push('data1', None)
data = stack.pop()

print(stack.top)

print(data)
'data1'

stack = Stack()
stack.push('data1', None)
stack.push('data2', None)
data = stack.pop()
print(stack.top.data)
print(data)
