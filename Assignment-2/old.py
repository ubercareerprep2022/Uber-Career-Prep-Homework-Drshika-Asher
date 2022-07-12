#4 - Implement the insert() and find() methods in the following simple binary search tree class:

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, root_node):
        self.root = root_node
#    Inserts a key into this binary search tree.
#    If there are n nodes in the tree, then the average runtime of this method should be log(n).
#    @param key The key to insert.
    def insert(self, subr, key: int):
        if self.root is None:
            self.root == Node(key)
        if subr is None:
            subr = Node(key)
        if subr.key > key:
            self.insert(subr.left, key)
        else:
            self.insert(subr.right, key)
#    Checks whether or not a key exists in this binary search tree.
#    If there are n nodes in the tree, then the average runtime of this method should be log(n).
#    @param key The key to check for.
#    @return true if the key is present in this binary search tree, false otherwise.
# psuedocode: traverse left if key is less than root, traverse right if key is greater than root, return subr if root = key
# def find(subroot, key):
#     if subroot == None:
#         return subroot
#     if subroot.left == None and subroot.right == None:
#         return subroot
#     elif subroot.key == key:
#         return subroot
#     elif key <  subroot.key:
#         subr = subroot.left
#         return find(subr, key)
#     elif key > subroot.key:  
#         subr = subroot.right 
#         return find(subr, key)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key)
        inorder(root.right)

# Driver program to test the above functions
# Let us create the following BST
#       50
#    /     \
#   30     70
#  / \     / \
# 20 40   60 80

r = Node(50)
bst = BinarySearchTree(r)
bst.insert(bst.root,30)
bst.insert(bst.root,70)
bst.insert(bst.root,80)
bst.insert(bst.root,20)
bst.insert(bst.root,40)
bst.insert(bst.root,60)

inorder(bst.root)
