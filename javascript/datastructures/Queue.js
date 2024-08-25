/*
   Queue.js is FIFO
   enqueue method adds node to the end of queue
   dequeue method removes node from beginning for queue
   */

class Node{
    constructor(val){
        this.val = val;
        this.next = null;
    }
}

class Queue{
    constructor(){
        this.first = null;
        this.last = null;
        this.length = 0;
    }
    enqueue(val){
        var newNode = new Node(val);
        if (!this.first) {
            this.first = newNode;
            this.last = newNode;
        } else {
            this.last.next = newNode;
            this.last = newNode;
        }
        this.length++;
        return this;
    }
    dequeue(){
        if (!this.first) return null;
        if (this.first === this.last) {
            this.last = null;
        }
        var poppedNode = this.first;
        this.first = poppedNode.next;
        poppedNode.next = null;
        this.length--;
        return poppedNode;
    }
    print_array(){
        var arr = [];
        var current = this.first;
        while(current) {
            arr.push(current.val);
            current = current.next
        }
        return arr;
    }
}

q1 = new Queue();

q1.enqueue(10);
console.log(q1.print_array());
q1.enqueue(20);
console.log(q1.print_array());
q1.enqueue(30);
console.log(q1.print_array());
q1.enqueue(40);
console.log(q1.print_array());

q1.dequeue();
console.log(q1.print_array());
q1.dequeue();
q1.dequeue();
console.log(q1.print_array());