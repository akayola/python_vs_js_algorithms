# stack.py 
# stack implemented using singly linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'{type(self).__name__}({self.data!r}, {self.next!r})'

class Stack(Node):
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __repr_(self):
        return f'{type(self).__name__}({self.first!r}, {self.last!r}, {self.length!r})'

    def push(self, data):
        newNode = Node(data)
        if not self.first:
            self.first = newNode
            self.last = newNode
        else:
            currentFirst = self.first
            self.first = newNode
            newNode.next = currentFirst

        self.length += 1
        return self 

    def pop(self):
        if not self.first: return None
        if self.first == self.last:
            self.last = None

        poppedNode = self.first
        self.first = poppedNode.next
        poppedNode.next = None
        self.length -= 1
        return poppedNode

    def print_stack(self):
        arr = []
        current = self.first
        while current:
            arr.append(current.data)
            current = current.next
        return arr


stack1 = Stack()
stack1.push(40)
stack1.push(30)
stack1.push(20)
stack1.push(10)

print(stack1.print_stack())

print(stack1.pop().data)
print(stack1.print_stack())
print(stack1.pop().data)
print(stack1.print_stack())
print(stack1.pop())
print(stack1.print_stack())
print(stack1.pop())
print(stack1.print_stack())
print(stack1.pop())
print(stack1.print_stack())
