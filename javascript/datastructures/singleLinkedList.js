/*
   Pushing Pseudocode:
   This function should accept a value.
   Create a new node using the value passed to the function.
   If there is no head property on the list,
   set the head and the tail to be newly created node.
   Otherwise set next property on the tail to be new node,
   and set the tail property on the list to be newly created node.
   Increment the length by one.
   Return the linked list.
*/
class Node{
    constructor(val) {
        this.val = val;
        this.next = null;
    }
}

class SinglyLinkedList{
    constructor() {
        this.head = null;
        this.tail = null;
        this.length = 0;
    }
    push(val) {
        var newNode = new Node(val);
        if (!this.head) {
            this.head = newNode;
            this.tail = this.head;
        } else {
            this.tail.next = newNode;
            this.tail = newNode;
        }
        this.length++;
        return this;
    }

    pop() {
        if (!this.head) return undefined;
        var current = this.head;
        var newTail = current;
        while (current.next) {
            newTail = current;
            current = current.next;
        }
        //console.log(current.val);
        //console.log(newTail.val);
        this.tail = newTail;
        this.tail.next = null;
        this.length--;
        if (this.length === 0) {
            this.head = null;
            this.tail = null;
        }
        return current;
    }

    shift() {
        if (!this.head) return undefined;
        var oldHead = this.head;
        this.head = oldHead.next;
        this.length--;
        if (this.length === 0) {
            this.tail = null;
        }
        return oldHead;
    }

    unshift(val) {
        var newNode = new Node(val);
        if (!this.head) {
            this.head = newNode;
            this.tail = newNode;
        } else {
            newNode.next = this.head;
            this.head = newNode;
        }
        this.length++;
        return this;
    }
    get(index) {
        if (index < 0 || index >= this.length) return null;
        var counter = 0;
        var current = this.head;
        while (counter != index) {
            current = current.next;
            counter++;
        }
        return current;
    }
    set(index, val) {
        var foundNode = this.get(index);
        if (foundNode) {
            foundNode.val = val;
            return true;
        }
        return false;
    }
    insert(index, val) {
        if (index < 0 || index > this.length) return false;
        if (index === this.length) return !!this.push(val);
        if (index === 0) return !!this.unshift(val);

        var newNode = new Node(val);
        var prevNode = this.get(index - 1);
        var tempNode = prevNode.next;
        prevNode.next = newNode;
        newNode.next = tempNode;
        this.length++;
        return true;
    }
    remove(index) {
        if (index < 0 || index >= this.length) return false;
        if (index === 0) return this.shift();
        if (index === this.length - 1) return this.pop();
        var prevNode = this.get(index - 1);
        var removedNode = prevNode.next;
        prevNode.next = removedNode.next;
        this.length--;
        return removedNode;
    }

    traverse() {
        var current = this.head;
        while (current) {
            console.log(current.val);
            current = current.next;
        }
    }
    reverse() {
        var node = this.head;
        this.head = this.tail;
        this.tail = node;
        var next = null;
        var prev = null;

        for (var i = 0; i < this.length; i++) {
            next = node.next;
            node.next = prev;
            prev = node;
            node = next;
        }
        return this;
    }
    //print function for troubelshooting only
    print() {
        var arr = [];
        var current = this.head;
        while (current) {
            arr.push(current.val);
            current = current.next;
        }
        console.log(arr);
    }
}

list1 = new SinglyLinkedList();
list1.push(10);
list1.push(20);
list1.push(30);
list1.push(40);


list1.traverse();
list1.reverse();
list1.print();


