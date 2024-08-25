/*
  BinarySearchTree.js
  */
 
class Node{
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

class BinarySearchTree{
    constructor() {
        this.root = null;
    }
    insert(value) {
        var newNode = new Node(value);
        if (this.root === null) {
            this.root = newNode;
            return this;
        } else {
            var current = this.root;
            while (true) {
                if (value === current.value) return null;
                if (value < current.value) {
                    if (current.left === null) {
                        current.left = newNode;
                        return this;
                    } else {
                        current = current.left;
                    }
                } else if (value > current.value) {
                    if (current.right === null) {
                        current.right = newNode;
                        return this;
                    } else {
                        current = current.right;
                    }
                }
            }
        }
    }
    find(value) {
        if (this.root === null) return false;
        var current = this.root;
        var found = false;

        while (current && !found) {
            if(value < current.value) {
                console.log("Looking for ", value, "at the Left");
                current = current.left;
            } else if (value > current.value) {
                console.log("Looking for ", value, "at the Right");
                current = current.right;
            } else {
                return true;
            }
        }
        if (!found) return false;
        console.log(current.value);
        return true;
    }
    BFS() {
        var node = this.root;
        var data = [];
        var queue = [];

        queue.push(node);
        while(queue.length) {
            node = queue.shift();
            data.push(node.value);
            if (node.left) queue.push(node.left);
            if (node.right) queue.push(node.right);
        }
        return data;
    }
    DFSPreOrder() {
        var current = this.root;
        var data = [];
        function traverse(node) {
            data.push(node.value);
            if (node.left) traverse(node.left);
            if (node.right) traverse(node.right);
        }
        traverse(current);
        return data;
    }
    DFSPostOrder() {
        var current = this.root;
        var data = [];
        function traverse(node) {
            if (node.left) traverse(node.left);
            if (node.right) traverse(node.right);
            data.push(node.value);
        }
        traverse(current);
        return data;
    }
    DFSInOrder() {
        var current = this.root;
        var data = [];
        
        function traverse(node) {
            if (node.left) traverse(node.left);
            data.push(node.value);
            if (node.right) traverse(node.right);
        }
        traverse(current);
        return data;
    }
}

tree = new BinarySearchTree();
tree.insert(10);
tree.insert(6);
tree.insert(3);
tree.insert(8);
tree.insert(15);
tree.insert(20);
tree.insert(13);

console.log(tree);

//console.log(tree.find(10));
//console.log(tree.find(11));
//console.log(tree.find(3));
//console.log(tree.find(2));
//console.log(tree.find(20));
//console.log(tree.find(17))

console.log("BFS", tree.BFS());
console.log("DFSPreOrder", tree.DFSPreOrder());
console.log("DFSPostOrder", tree.DFSPostOrder());
console.log("DFSInOrder", tree.DFSInOrder());