
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Preorder Traversal
def preorder(root):
    if root:
        print(root.data, end="")
        preorder(root.left)
        preorder(root.right)


# Inorder Traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end="")
        inorder(root.right)


# Postorder Traversal
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end="")


# Create Binary Tree
root = Node("R")

root.left = Node("E")
root.right = Node("H")

root.left.left = Node("Y")
root.left.right = Node("M")

root.right.left = Node("E")
root.right.right = Node("R")

root.left.left.left = Node("O")
root.left.left.right = Node("N")

root.left.right.left = Node("A")
root.left.right.right = Node("N")

root.right.left.left = Node("A")
root.right.right.left = Node("N")


# Display Results
print("Name: REYMON HERNAN")

print("\nPreorder:")
preorder(root)

print("\n\nInorder:")
inorder(root)

print("\n\nPostorder:")
postorder(root)
