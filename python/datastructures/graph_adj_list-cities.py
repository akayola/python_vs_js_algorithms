# graph_adj_list.py

class Graph:
    def __init__(self):
        self.adjList = {}
    
    def __repr__(self):
        return f'{type(self).__name__}({self.adjList!r})'

    def addVertex(self, vertex):
        if not self.adjList.get(vertex):
            self.adjList[vertex] = []

    def addEdge(self, vertex1, vertex2):
        if not self.adjList.get(vertex1):
            self.addVertex(vertex1)
        if not self.adjList.get(vertex2):
            self.addVertex(vertex2)

        self.adjList[vertex1].append(vertex2)
        self.adjList[vertex2].append(vertex1)

    def removeEdge(self, vertex1, vertex2):
        try:
            self.adjList[vertex1].remove(vertex2)
            self.adjList[vertex2].remove(vertex1)
        except ValueError:
            pass

    def removeVertex(self, vertex):
        while len(self.adjList[vertex]):
            adjVertex = self.adjList[vertex].pop()
            #print(adjVertex)
            self.adjList[adjVertex].remove(vertex)
        del self.adjList[vertex]


g = Graph()

g.addVertex("Tokyo")

g.adjList["Tokyo"].append("Marlboro")

#print(g)
print(f'type of g: {type(g)}')
print(f'type of g.addVertex: {type(g.addVertex)}')
print(f'type of g.adjList: {type(g.adjList)}')
print(f'type of g.adjList["Tokyo"]: {type(g.adjList["Tokyo"])}')
print(f'g.adjList["Tokyo"]: {g.adjList["Tokyo"]}')
print(f'g.adjList["Tokyo"][0]: {g.adjList["Tokyo"][0]}')
print(f'g.adjList.get("Tokyo")[0]: {g.adjList.get("Tokyo")[0]}')

g.addEdge("Dallas", "New York")
g.addEdge("Aspen", "Tokyo")
g.addEdge("New York", "Tokyo")
g.addEdge("Aspen", "Dallas")
g.addEdge("New York", "Marlboro")
g.addEdge("New York", "Hong Kong")
g.addEdge("Tokyo", "Hong Kong")
print(g)

g.removeVertex("Aspen")
print(g)
g.removeVertex("Hong Kong")
print(g)
