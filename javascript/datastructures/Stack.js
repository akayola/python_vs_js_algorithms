/*
   Stack.js is LIFO
   push method adds new Node to beginning of the stack
   pop method removes node from beginning of the stack
   Insertion O(1)
   Removal O(1)
*/

class Node{
    constructor(val) {
        this.val = val;
        this.next = null;
    }
}

class Stack {
    constructor() {
        this.first = null;
        this.last = null;
        this.length = 0;
    }
    push(val) {
        var newNode = new Node(val);
        if (!this.first) {
            this.first = newNode;
            this.last = newNode;
        } else {
            var currentNode = this.first;
            this.first = newNode;
            newNode.next = currentNode;
        }
        this.length++;
        return this;      
    }
    pop() {
        if (!this.first) return undefined;
        var poppedNode = this.first;
        if (this.first === this.last) {
            this.last = null;
        }
        this.first = poppedNode.next;
        poppedNode.next = null;
        this.length--;
        return poppedNode;
    }
    print_stack() {
        var arr = [];
        var current = this.first;
        while (current) {
            arr.push(current.val);
            current = current.next;
        }
        return arr;
    }
}

stack1 = new Stack();
stack1.push(10);
stack1.push(20);
stack1.push(30);
stack1.push(40);

console.log(stack1.pop());
console.log(stack1.print_stack());
console.log(stack1.pop());
console.log(stack1.print_stack());
console.log(stack1.pop());
console.log(stack1.print_stack());
console.log(stack1.pop());
console.log(stack1.print_stack());
console.log(stack1.pop());
console.log(stack1.print_stack());