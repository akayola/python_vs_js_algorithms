'''
   BinarySearchTree.py
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinarySearchTree(Node):
    def __init__(self):
        self.root = None

    def insert(self, value):
        newNode = Node(value)
      
        if self.root == None:
            self.root = newNode
            return self
        else:
            current = self.root
            while True:
                if value == current.value: return None
                if value < current.value:
                    if current.left == None:
                        current.left = newNode
                        return self
                    else:
                        current = current.left

                elif value > current.value:
                    if current.right == None:
                        current.right = newNode
                        return self
                    else:
                        current = current.right

    def find(self, value):
        if self.root == None:
            return False

        current = self.root
        found = False

        if value == self.root.value:
            print(f'Found {value} at ROOT')

        while current and not found:
            if value < current.value:
                print(f'Looking for {value} at LEFT')
                current = current.left

            elif value > current.value:
                print(f'Looking for {value} at RIGHT')
                current = current.right
            else:
                return True
        if not found:
            return False
        print(current.value)
        return True

    def BFS(self):
        node = self.root
        data = []
        queue = []

        queue.append(node)

        while len(queue) != 0:
            node = queue.pop(0)
            data.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return data

    def DFSPreOrder(self):
        current = self.root
        data = []
        
        def traverse(node):
            data.append(node.value)
            if node.left: traverse(node.left)
            if node.right: traverse(node.right)
        traverse(current)
        return data

    def DFSPostOrder(self):
        current = self.root
        data = []

        def traverse(node):
            if node.left:  traverse(node.left)
            if node.right: traverse(node.right) 
            data.append(node.value)
        traverse(current)
        return data

    def DFSInOrder(self):
        current = self.root
        data = []

        def traverse(node):
            if node.left: traverse(node.left)
            data.append(node.value)
            if node.right: traverse(node.right)
        traverse(current)
        return data

tree = BinarySearchTree()

tree.insert(10)
tree.insert(6)
tree.insert(3)
tree.insert(8)
tree.insert(15)
tree.insert(20)

print(tree.root.value)
print(tree.root.left.value)
print(tree.root.left.right)
print(tree.root.right.value)

print(tree.find(10))
print(tree.find(9))
print(tree.find(6))
print(tree.find(3))
print(tree.find(8))
print(tree.find(15))
print(tree.find(20))

print(tree.BFS())
print(tree.DFSPreOrder())
print(tree.DFSPostOrder())
print(tree.DFSInOrder())
