class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
    
    def __repr_(self):
        return f'{type(self).__name__}({self.data}, {self.next})'


class SinglyLinkedList(Node):
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __repr__(self):
        return f'{type(self).__name__}({self.head}, {self.tail}, {self.length})'

    def push(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
            self.tail = newNode 
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1
        return self

    def pop(self):
        if not self.head:
            return None
        current = self.head
        new_tail = current
        while current.next:
            new_tail = current
            current = current.next
        self.tail = new_tail
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return current

    def shift(self):
        if not self.head:
            return None
        oldHead = self.head
        self.head = oldHead.next
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return oldHead

    def unshift(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1
        return self

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        counter = 0
        current = self.head
        while counter != index:
            current = current.next
            counter += 1
        return current

    def set(self, index, data):
        foundNode = self.get(index)
        if foundNode:
            foundNode.data = data
            return True
        return False

    def insert(self, index, data):
        if index < 0 or index > self.length: return False
        if index == self.length:
            self.push(data)
            return True
        if index == 0:
            self.unshift(data)
            return True

        newNode = Node(data)
        prevNode = self.get(index - 1)
        tempNode = prevNode.next
        prevNode.next = newNode
        newNode.next = tempNode
        self.length += 1
        return True

    def reverse(self):
        node = self.head
        self.head = self.tail
        self.tail = node
        next = None
        prev = None
        step = 1

        print(f'node: {node.data}, self.head: {self.head.data}, self.tail: {self.tail.data}')
     
        for i in range(self.length):
            print(f'step: {step}')

            next = node.next
            try:
                print(f'node: {node.data}, next: {node.next.data}')
            except AttributeError:
                print(f'node: {node.data}, next: {node.next}') 

            node.next = prev
            try:
                print(f'node.next: {node.next.data}, prev: {prev.data}')
            except AttributeError:
                print(f'node.next: {node.next}, prev: {prev}')

            prev = node
            try:
                print(f'prev: {prev.data}, node: {node.data}')
            except AttributeError:
                print(f'prev: {prev}, node: {node.data}')

            node = next
            try:
                print(f'node: {node.data}, next: {next.data}')
            except AttributeError:
                print(f'node: {node}, next: {next}')

            step += 1
            print("")

        return self

    # print_array function for troubleshooting only
    def print_array(self):
        arr = []
        current = self.head
        while current:
            arr.append(current.data)
            current = current.next
        return arr

    def traverse(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


list1 = SinglyLinkedList()

list1.push("100")
list1.push("200")
list1.push("300")
list1.push("400")
list1.push("500")

list1.reverse()
print(list1.print_array())
#list1.traverse()
