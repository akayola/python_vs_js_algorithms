class Node{
    constructor(val){
        this.val = val;
        this.next = null;
        this.prev = null;
    }
}

class DoublyLinkedList{
    constructor() {
        this.head = null;
        this.tail = null;
        this.length = 0;
    }
    push(val) {
        var newNode = new Node(val);
        //if (this.length === 0) {
        if (!this.head) {
            this.head = newNode;
            this.tail = newNode;
        } else {
            this.tail.next = newNode;
            newNode.prev = this.tail;
            this.tail = newNode;
        }
        this.length++;
        return this;
    }
    pop() {
        if (!this.head) return undefined;
        var poppedNode = this.tail;
        if (this.length === 1) {
            this.head = null;
            this.tail = null;
        } else {
            this.tail = poppedNode.prev;
            this.tail.next = null;
            poppedNode.prev = null;
        }
        this.length--;
        return poppedNode;
    }
    shift() {
        if (!this.head) return undefined;
        var oldHead = this.head;
        if (this.length === 1) {
            this.head = null;
            this.tail = null;
        } else {
            this.head = oldHead.next;
            this.head.prev = null;
            oldHead.next = null;
        }
        this.length--;
        console.log(this.length);
        return oldHead; 
    }
    unshift(val) {
    var newNode = new Node(val);
    if (!this.head) {
        this.head = newNode;
        this.tail = newNode;
    } else {
        this.head.prev = newNode;
        newNode.next = this.head;
        this.head = newNode;
    }
    this.length++;
    return this;
    }
    get(index) {
        if (index < 0 || index >= this.length) return null;
        if (index <= Math.floor(this.length / 2)) {
            console.log("WORKING FROM BEGINNING!!!");
            var count = 0;
            var current = this.head;
            while (count !== index) {
                current = current.next;
                count++;
            }
            //return current;
        } else {
            console.log("WORKING FROM END!!!");
            var count = this.length - 1;
            var current = this.tail;
            while (count !== index) {
                current = current.prev;
                count--;
            }
            //return current;
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
        if (index === 0) return !!this.unshift(val);
        if (index === this.length) return !!this.push(val);

        var newNode = new Node(val);
        var beforeNode = this.get(index - 1);
        var afterNode = beforeNode.next;

        beforeNode.next = newNode;
        newNode.prev = beforeNode;
        newNode.next = afterNode;
        afterNode.prev = newNode;
        this.length++;
        return true;
    }
    remove(index) {
        if (index < 0 || index >= this.length) return undefined;
        if (index === 0) return this.shift();
        if (index === this.length - 1) return this.pop();

        var removedNode = this.get(index);
        var beforeNode = removedNode.prev;
        var afterNode = removedNode.next;

        beforeNode.next = afterNode;
        afterNode.prev = beforeNode;
        //removedNode.prev.next = removedNode.next
        //removedNode.next.prev = removedNode.prev
        removedNode.next = null;
        removedNode.prev = null;
        this.length--;
        return removedNode;
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
    // print function for troubleshooting only
    print() {
        var arr = [];
        var current = this.head;
        while (current) {
            arr.push(current.val);
            current = current.next;
        }
        return arr;
    }
}

list1 = new DoublyLinkedList();
list1.push(10);
list1.push(20);
list1.push(30);
list1.push(40);
list1.push(50);
list1.push(60);
list1.push(70);

//console.log(list1);

console.log(list1.print());
console.log(list1.reverse());
console.log(list1.print());