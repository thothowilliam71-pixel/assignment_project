class Node:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None
class BST:
    def insert(self, root, name):
        if root is None:
            return Node(name)
        if name < root.name:
            root.left = self.insert(root.left, name)
        else:
            root.right = self.insert(root.right, name)
        return root
    def search(self, root, name):
        if root is None or root.name == name:
            return root
        if name < root.name:
            return self.search(root.left, name)
        return self.search(root.right, name)
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.name, end=" ")
            self.inorder(root.right)
tree = BST()
root = None
root = tree.insert(root, "John")
root = tree.insert(root, "Alice")
root = tree.insert(root, "Zack")
print("In-order traversal:")
tree.inorder(root)
print("\nSearch result:")
result = tree.search(root, "Alice")
print("Found" if result else "Not found")