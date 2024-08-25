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

    def depthFirstRecursive(self, start):
        result = []
        visited = {}

        def dfs(vertex):
            if not vertex:
                return None

            visited[vertex] = True
            result.append(vertex)

            for value in self.adjList[vertex]:
                if not value in visited:
                    return dfs(value)

            for value in self.adjList:
                if not value in visited:
                    return dfs(value)
            return result 
        return dfs(start)

    def depthFirstIterative(self, start):
        stack = [start]
        visited = {}
        result = []
        currentVertex = None
        visited[start] = True

        while len(stack):
            currentVertex = stack.pop()
            result.append(currentVertex)
            
            for value in self.adjList[currentVertex]:
                if not value in visited:
                    visited[value] = True
                    stack.append(value)
        return result

    def bredthFirsRecursive(self, start):
        result = []
        visited = {}

        def bfs(vertex):
            if not vertex:
                return None

            visited[vertex] = True
            result.append(vertex)

            for value in self.adjList:
                if not value in visited:
                    return bfs(value)
            return result
        return bfs(start)

    def bredthFirstIterative(self, start):
        queue = []
        result = []
        visited = {}
        currentVertex = None

        queue.append(start)
        visited[start] = True

        while len(queue):
            currentVertex = queue.pop(0)
            result.append(currentVertex)
            
            for value in self.adjList:
                if not value in visited:
                    visited[value] = True
                    queue.append(value)
        return result


g = Graph()

g.addVertex("A")
g.addVertex("B")
g.addVertex("C")
g.addVertex("D")
g.addVertex("E")
g.addVertex("F")

g.addEdge("A", "B")
g.addEdge("A", "C")
g.addEdge("B", "D")
g.addEdge("C", "E")
g.addEdge("D", "E")
g.addEdge("D", "F")
g.addEdge("E", "F")

#print(g)

import cProfile

cProfile.run('print("Depth First Graph Traversal (Recursive):", g.depthFirstRecursive("A"))')
cProfile.run('print("Depth First Graph Traversal (Iterative):", g.depthFirstIterative("A"))')

cProfile.run('print("Bredth First Graph Traversal (Recursive)", g.bredthFirsRecursive("A"))')
cProfile.run('print("Bredth First Graph Traversal (Iterative)", g.bredthFirstIterative("A"))')

print("Depth First Graph Traversal (Recursive):", g.depthFirstRecursive("A"))
print("Depth First Graph Traversal (Iterative):", g.depthFirstIterative("A"))

print("Bredth First Graph Traversal (Recursive)", g.bredthFirsRecursive("A"))
print("Bredth First Graph Traversal (Iterative)", g.bredthFirstIterative("A"))
