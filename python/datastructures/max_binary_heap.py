# max_binary_heap.py

class MaxBinaryHeap:
    def __init__(self):
        #self.values = []
        self.values = [41, 39, 33, 18, 27, 12]

    def insert(self, element):
        self.values.append(element)
        self.bubbleUp()

    def bubbleUp(self):
        idx = len(self.values) - 1
        element = self.values[idx]

        while idx > 0:
            parentIdx = (idx - 1) // 2
            print(parentIdx)
            parent = self.values[parentIdx]
            if element <= parent: break
            self.values[parentIdx] = element
            self.values[idx] = parent
            idx = parentIdx
        
    def extractMax(self):
        max = self.values[0]
        end = self.values.pop()
        if len(self.values) > 0:
            self.values[0] = end
            self.bubbleDown()
        return max

    def bubbleDown(self):
        idx = 0
        length = len(self.values)
        element = self.values[0]

        while True:
            leftChildIdx = idx * 2 + 1
            rightChildIdx = idx * 2 + 2
            leftChild = None
            rightChild = None
            swap = None

            if leftChildIdx < length:
                leftChild = self.values[leftChildIdx]
                swap = leftChildIdx

            if rightChildIdx < length:
                rightChild = self.values[rightChildIdx]

                if (
                    (swap == None and rightChild > element) or
                    (swap != None and rightChild > leftChild)
                   ):
                    swap = rightChildIdx
 
            if swap == None: break
            self.values[idx] = self.values[swap]
            self.values[swap] = element
            idx = swap

 

heap = MaxBinaryHeap()
print(heap.values)
heap.insert(55)
print(heap.values)

print(heap.extractMax())
print(heap.values)

print(heap.extractMax())
print(heap.values)

