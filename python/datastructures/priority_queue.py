#priority_queue.py

class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

    def __repr__(self):
        return f'{type(self).__name__}({self.value!r}, {self.priority!r})'

class PriorityQueue(Node):
    def __init__(self):
        self.values = []

    def __repr__(self):
        return f'{type(self).__name}({self.values!r})'


    def enqueue(self, value, priority):
        newNode = Node(value, priority)
        self.values.append(newNode)
        self.bubbleUp()

    def bubbleUp(self): 
        idx = len(self.values) - 1
        element = self.values[idx]

        while idx > 0:
            parentIdx = (idx - 1) // 2
            parent = self.values[parentIdx]
            if element.priority >= parent.priority: break
            self.values[parentIdx] = element
            self.values[idx] = parent
            idx = parentIdx

    def dequeue(self):
        min = self.values[0]
        end = self.values.pop()
        if len(self.values) > 0:
            self.values[0] = end
            self.bubbleDown()
        return min

    def bubbleDown(self):
        idx = 0
        length = len(self.values)
        element = self.values[idx]

        while True:
            leftChildIdx = idx * 2 + 1
            rightChildIdx = idx * 2 + 2
            leftChild = None
            rightChild = None
            swap = None
           
            if leftChildIdx < length:
                leftChild = self.values[leftChildIdx]
                print(f'leftChildIdx: {leftChildIdx}')
                        #leftChild.value: {lefChild.value}, +
                        #leftChild.priority: {lefChild.priority}')
                if leftChild.priority < element.priority:
                    swap = leftChildIdx

            if rightChildIdx < length:
                rightChild = self.values[rightChildIdx]
                print(f'rightChildIdx: {rightChildIdx}')
                        #rightChild.value: {rightChild.value},
                        #rightChild.priority: {rightChild.priority}')
                if (
                     (swap == None and rightChild.priority < element.priority) or
                     (swap != None and rightChild.priority < leftChild.priority) 
                   ):
                    swap = rightChildIdx

            if swap == None: break
            self.values[idx] = self.values[swap]
            self.values[swap] = element
            idx = swap


tasks = PriorityQueue()

tasks.enqueue("Task 2", 2)
tasks.enqueue("Task 3", 3)
tasks.enqueue("Task 1", 1)
tasks.enqueue("Task 5", 5)
tasks.enqueue("Task 4", 4)

print(tasks.values)             

print(tasks.dequeue())
tasks.enqueue("Task 6", 6)

print(tasks.values)             

print(tasks.dequeue())

print(tasks.values)             

