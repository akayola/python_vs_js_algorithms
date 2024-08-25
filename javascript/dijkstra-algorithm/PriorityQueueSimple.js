/*
  PriorityQueueNaive.js
  Sorting O(N * logN)
*/

class PriorityQueue {
    constructor() {
        this.values = [];
    }
    enqueue (value, priority) {
        this.values.push({value, priority});
        this.sort();
    };
    dequeue() {
        return this.values.shift();
    };
    sort() {
        this.values.sort((a, b) => a.priority - b.priority);
    };
}

q = new PriorityQueue();
q.enqueue("C", 12);
q.enqueue("B", 5);
q.enqueue("E", 20);
q.enqueue("A", 2);
q.enqueue("D", 15);

console.log(q);
console.log(q.dequeue());
console.log(q.values);
