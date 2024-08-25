# doubly_linked_list.py

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    #def __repr__(self):
    #    return f'{type(self).__name__}({self.data!r}, {self.next!r}, {self.prev!r})'

class DoublyLinkedList(Node):
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    #def __repr__(self):
    #    return f'{type(self).__name__}({self.head!r}, {self.tail!r}, {self.length!r})'

    def push(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        self.length += 1
        return self

    def pop(self):
        if not self.head: return None
        poppedNode = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = poppedNode.prev
            self.tail.next = None
            poppedNode.prev = None
        self.length -= 1
        return poppedNode

    def shift(self):
        if not self.head: return None
        oldHead = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = oldHead.next
            self.head.prev = None
            oldHead.next = None
        self.length -= 1
        return oldHead

    def unshift(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
        self.length += 1
        return self 
     
    def get(self, index):
        if index < 0 or index >= self.length: return None
        if index <= self.length // 2:
            print("WORKING FROM BEGINNING!!!")
            count = 0
            current = self.head
            while count != index:
                current = current.next
                count += 1
        else:
            print("WORKING FROM END!!!")
            count = self.length - 1
            current = self.tail
            while count != index:
                current = current.prev
                count -= 1
        return current

    def set(self, index, data):
        foundNode = self.get(index)
        if foundNode != None:
            foundNode.data = data
            return True
        return False

    def insert(self, index, data):
        if index < 0 or index > self.length: return False

        if index == 0:
            self.unshift(data)
            return True

        if index == self.length:
            self.push(data)
            return True

        newNode = Node(data)
        beforeNode = self.get(index - 1)
        afterNode = beforeNode.next
        beforeNode.next = newNode

        newNode.prev = beforeNode
        newNode.next = afterNode
        afterNode.prev = newNode

        self.length += 1
        return True        
    
    def remove(self, index):
        if index < 0 or index >= self.length: return None
        if index == 0: return self.shift()
        if index == self.length - 1: return self.pop()

        removedNode = self.get(index)
        beforeNode = removedNode.prev
        afterNode = removedNode.next

        beforeNode.next = afterNode
        afterNode.prev = beforeNode
        removedNode.next = None
        removedNode.prev = None
   
        self.length -= 1
        return removedNode

    def reverse(self):
        node = self.head
        self.head = self.tail
        self.tail = node
        next = None
        prev = None

        for i in range(self.length):
            next = node.next
            node.next = prev
            prev = node
            node = next
        return self 

    def print_array(self):
        arr = []
        current = self.head
        while current:
            arr.append(current.data)
            current = current.next
        return arr

list1 = DoublyLinkedList()

list1.push(10)
list1.push(20)
list1.push(30)
list1.push(40)
list1.push(50)
list1.push(60)
list1.push(70)
list1.push(80)
list1.push(90)


print(list1.print_array())
list1.reverse()
print(list1.print_array())
