class WeightedGraph {
    constructor() {
        this.adjacencyList = {};
    }
    addVertex(vertex) {
        if (!this.adjacencyList[vertex]) {
            this.adjacencyList[vertex] = [];
        }
    }
    addEdge(vertex1, vertex2, weight) {
        this.adjacencyList[vertex1].push({node:vertex2, weight:weight});
        this.adjacencyList[vertex2].push({node:vertex1, weight:weight});
    }
}

g = new WeightedGraph();
g.addVertex("A");
g.addVertex("B");
g.addVertex("C");

g.addEdge("A", "B", 10);
g.addEdge("A", "C", 15);
g.addEdge("B", "C", 12);

console.log(g);