class Node {
    constructor(value, priority) {
        this.value = value;
        this.priority = priority;
    }
}
class PriorityQueue {
    constructor() {
        this.values = [];
    }
    enqueue(value, priority) {
        let newNode = new Node(value, priority);
        this.values.push(newNode);
        this.bubbleUp();
    }
    bubbleUp() {
        let idx = this.values.length - 1;
        const element = this.values[idx]
        //console.log(element, element.priority);
        while (idx > 0) {
            let parentIdx = Math.floor((idx - 1) / 2);
            let parent = this.values[parentIdx];
            if (element.priority >= parent.priority) break;
            this.values[parentIdx] = element;
            this.values[idx] = parent;
            idx = parentIdx;
        }
    }    
    dequeue() {
        const min = this.values[0];
        const end = this.values.pop();
        if (this.values.length > 0) {
            this.values[0] = end;
            this.bubbleDown();
        }
        return min;
    }
    bubbleDown() {
        let idx = 0;
        const length = this.values.length;
        const element = this.values[0];
        while (true) {
            let leftChildIdx = idx * 2 + 1;
            let rightChildIdx = idx * 2 + 2;
            let leftChild, rightChild;
            let swap = null;

            if (leftChildIdx < length) {
                leftChild = this.values[leftChildIdx];
                if (leftChild.priority < element.priority) {
                    swap = leftChildIdx;
                }
            }
            if (rightChildIdx < length) {
                rightChild = this.values[rightChildIdx];
                if (
                    (swap === null && rightChild.priority < element.priority) ||
                    (swap !== null && rightChild.priority < leftChild.priority)
                ) {
                    swap = rightChildIdx;
                }
            }
            if (swap === null) break;
            this.values[idx] = this.values[swap];
            this.values[swap] = element;
            idx = swap;
        }
    }
}


let tasks = new PriorityQueue();

tasks.enqueue("Task 5", 5);
tasks.enqueue("Task 1", 1);
//tasks.enqueue("Task 6", 6);
tasks.enqueue("Task 2", 2);
tasks.enqueue("Task 4", 4);
tasks.enqueue("Task 3", 3);

console.log(tasks.values);

console.log(tasks.dequeue());
console.log(tasks.dequeue());
tasks.enqueue("Task 6", 6);
console.log(tasks.dequeue());
//console.log(tasks.dequeue());

console.log(tasks.values);
for (i = 0; i <+ tasks.values.length -1; i++) console.log(tasks.values[i]);