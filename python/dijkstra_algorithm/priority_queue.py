# priority_queue.py

class PriorityQueue:
    def __init__(self):
        self.values = []

    def __repr__(self):
        return f'{type(self).__name__}({self.values!r})'

    def enqueue(self, value, priority):
        self.values.append({value: priority})
        #self.sort()

    def dequeue(self):
        return self.values.pop(0)


q = PriorityQueue()

q.enqueue("C", 10)
q.enqueue("B", 3)
q.enqueue("A", 0)
q.enqueue("D", 15)
q.enqueue("E", 12)
q.enqueue("F", 7)
print(q)

q.dequeue()
print(q)
