# Dijstra's algorithm to find shortest path
# Using binary heap for priority queue.

import math

infinity = math.inf

class WeightedGraph:
    def __init__(self):
        self.adjacencyList = {}

    def __repr__(self):
        return f'{type(self).__name__}({self.adjacencyList!r})'

    def addVertex(self, vertex):
        if not self.adjacencyList.get(vertex):
            self.adjacencyList[vertex] = []
    
    def addEdge(self, vertex1, vertex2, weight):
        self.adjacencyList[vertex1].append({'node':vertex2, 'weight':weight})
        self.adjacencyList[vertex2].append({'node':vertex1, 'weight':weight})

    def Dijkstra(self, start, finish):
        nodes = PriorityQueue()
        # Methods of PriorityQueue(Node):
        # bubbleDown, bubbleUp, dequeue, enqueue, values
        #print(dir(nodes))

        distances = {}
        previous = {}
        path = []
        smallest = None

        for vertex in self.adjacencyList:
            if vertex == start:
                # Set start vertex: 0 in distances dictionary
                # {'A': 0}
                distances[vertex] = 0
                #print(f'distances: {distances}')
                
                # Append start vertex with highes priority (0) to self.values list 
                # [Node('A', 0)]
                nodes.enqueue(vertex, 0)
                #print(f'nodes.values: {nodes.values}')

            else:
                # For rest of vertices set:
                # distances: 'B': inf, 'C': inf, 'D': inf, 'E': inf, 'F': inf
                # nodes.values: Node('B', inf), Node('C', inf), Node('D', inf), Node('E', inf), Node('F', inf)   
                distances[vertex] = infinity
                nodes.enqueue(vertex, infinity)

            previous[vertex] = None

        #print(f'distances: {distances}')
        #distances: {'A': 0, 'B': inf, 'C': inf, 'D': inf, 'E': inf, 'F': inf}

        #print(f'nodes.values: {nodes.values}')
        #nodes.values: [Node('A', 0), Node('B', inf), Node('C', inf), Node('D', inf), Node('E', inf), Node('F', inf)]

        #print(f'previous: {previous}')
        #previous: {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None}

        while len(nodes.values):
            smallest = nodes.dequeue().value

            #print(f'smallest: {smallest}')
            #smallest: A
            #smallest: C
            #smallest: B
            #smallest: D
            #smallest: F
            #smallest: F
            #smallest: E

            if smallest == finish:
                # We are Done. Build up path and return at the end.
                while previous[smallest]:
                    path.append(smallest)
                    smallest = previous[smallest]

                    #print(f'smallest: {smallest}')
                    #smallest: F
                    #smallest: D
                    #smallest: C
                    #smallest: A 

                break

            #print(f'smallest: {smallest}, distance: {distances[smallest]}')
            #smallest: A, distance: 0
            #smallest: C, distance: 2
            #smallest: B, distance: 4
            #smallest: D, distance: 4
            #smallest: F, distance: 5
            #smallest: F, distance: 5

            if smallest or distances[smallest] != inf:

                #print(self.adjacencyList[smallest])
                #[{'node': 'B', 'weight': 4}, {'node': 'C', 'weight': 2}]
                #[{'node': 'A', 'weight': 2}, {'node': 'D', 'weight': 2}, {'node': 'F', 'weight': 4}]
                #[{'node': 'A', 'weight': 4}, {'node': 'E', 'weight': 3}]
                #[{'node': 'C', 'weight': 2}, {'node': 'E', 'weight': 3}, {'node': 'F', 'weight': 1}]
                #[{'node': 'C', 'weight': 4}, {'node': 'D', 'weight': 1}, {'node': 'E', 'weight': 1}]
                #[{'node': 'C', 'weight': 4}, {'node': 'D', 'weight': 1}, {'node': 'E', 'weight': 1}]

                for neighbor in range(len(self.adjacencyList[smallest])):
                    # find neighbor node
                    nextNode = self.adjacencyList[smallest][neighbor]

                    #print(f'nextNode: {nextNode}')
                    #nextNode: {'node': 'B', 'weight': 4}
                    #nextNode: {'node': 'C', 'weight': 2}
                    #nextNode: {'node': 'A', 'weight': 2}
                    #nextNode: {'node': 'D', 'weight': 2}
                    #nextNode: {'node': 'F', 'weight': 4}
                    #nextNode: {'node': 'A', 'weight': 4}
                    #nextNode: {'node': 'E', 'weight': 3}
                    #nextNode: {'node': 'C', 'weight': 2}
                    #nextNode: {'node': 'E', 'weight': 3}
                    #nextNode: {'node': 'F', 'weight': 1}
                    #nextNode: {'node': 'C', 'weight': 4}
                    #nextNode: {'node': 'D', 'weight': 1}
                    #nextNode: {'node': 'E', 'weight': 1}
                    #nextNode: {'node': 'C', 'weight': 4}
                    #nextNode: {'node': 'D', 'weight': 1}
                    #nextNode: {'node': 'E', 'weight': 1}

                    # calculate distance to neighboring node
                    candidate = distances[smallest] + nextNode['weight']

                    #print(f'candidate: {candidate}')
                    #candidate: 4
                    #candidate: 2
                    #candidate: 4
                    #candidate: 4
                    #candidate: 6
                    #candidate: 8
                    #candidate: 7
                    #candidate: 6
                    #candidate: 7
                    #candidate: 5
                    #candidate: 9
                    #candidate: 6
                    #candidate: 6
                    #candidate: 9
                    #candidate: 6
                    #candidate: 6

                    nextNeighbor = nextNode['node']

                    #print(f'nextNeighbor: {nextNeighbor}')
                    #nextNeighbor: B
                    #nextNeighbor: C
                    #nextNeighbor: A
                    #nextNeighbor: D
                    #nextNeighbor: F
                    #nextNeighbor: A
                    #nextNeighbor: E
                    #nextNeighbor: C
                    #nextNeighbor: E
                    #nextNeighbor: F
                    #nextNeighbor: C
                    #nextNeighbor: D
                    #nextNeighbor: E
                    #nextNeighbor: C
                    #nextNeighbor: D
                    #nextNeighbor: E

                    if candidate < distances[nextNeighbor]:
                        # update new smalles distance to neighbor
                        distances[nextNeighbor] = candidate

                        # update previous dictionary - How to get to neighbor
                        previous[nextNeighbor] = smallest

                        # enqueu in priority queue with new priority
                        nodes.enqueue(nextNeighbor, candidate)

        path.append(smallest)
        reversed_path = list(reversed(path)) 
        return reversed_path
   
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
        return f'{self(type).__name__}({self.values!r})'
    
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
            if element.priority >= parent.priority:
                break
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
                #print(f'leftChildIdx: {leftChildIdx}')
                        #leftChild.value: {lefChild.value}, +
                        #leftChild.priority: {lefChild.priority}')
                if leftChild.priority < element.priority:
                    swap = leftChildIdx

            if rightChildIdx < length:
                rightChild = self.values[rightChildIdx]
                #print(f'rightChildIdx: {rightChildIdx}')
                        #rightChild.value: {rightChild.value}, +
                        #rightChild.priority: {rightChild.priority}')
                if (
                     (swap == None and rightChild.priority < element.priority) or
                     (swap != None and rightChild.priority < leftChild.priority)
                   ):
                    swap = rightChildIdx

            if swap == None:
                break
            self.values[idx] = self.values[swap]
            self.values[swap] = element
            idx = swap

graph = WeightedGraph()

graph.addVertex("A")
graph.addVertex("B")
graph.addVertex("C")
graph.addVertex("D")
graph.addVertex("E")
graph.addVertex("F")

graph.addEdge("A", "B", 4)
graph.addEdge("A", "C", 2)
graph.addEdge("B", "E", 3)
graph.addEdge("C", "D", 2)
graph.addEdge("C", "F", 4)
graph.addEdge("D", "E", 3)
graph.addEdge("D", "F", 1)
graph.addEdge("E", "F", 1)

print(graph.Dijkstra("A", "E"))

#print(graph.Dijkstra("A", "F"))
#print(graph.Dijkstra("A", "B"))
#print(graph.Dijkstra("E", "A"))
#print(graph.Dijkstra("C", "B"))
#print(graph.Dijkstra("B", "C"))
#print(graph.Dijkstra("D", "A")) 
