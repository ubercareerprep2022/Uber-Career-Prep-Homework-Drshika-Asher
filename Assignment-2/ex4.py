#[Trees - Ex4] Exercise: Implement a binary search tree
#Implement the insert() and find() methods in the following simple binary search tree class:

from logging import root


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self, root:Node):
        self.root = root

    # Inserts a key into this binary search tree.
    # If there are n nodes in the tree, then the average runtime of this method should be log(n).
    # @param key The key to insert.
    # normally if i'd do this in c++, i would use find as a subroutine for insert because i can use take the mem address and assign a variable value.
    def insert(self, subroot, key):
        if subroot == None:
            return Node(key) #deciding to return the new root 
        else:
            if key < subroot.key:
                print(subroot.key)
                return self.insert(subroot.left, key)
            elif key >= subroot.key:
                print(subroot.key)
                return self.insert(subroot.right, key)
            return self.subroot


    # Checks whether or not a key exists in this binary search tree.
    # If there are n nodes in the tree, then the average runtime of this method should be log(n).

    # @param key The key to check for.
    # @return true if the key is present in this binary search tree, false otherwise.
    def find(self, subroot, key):
        if self.root == None or key == self.root.key:
            return True 
        if subroot == None:
            return False
        if subroot.key == key:
            return True
        elif key < subroot.key:
            return self.find(subroot.left, key)
        elif key >= subroot.key:
            return self.find(subroot.right, key)

# TESTING
sixteen = Node(16)
sixteen.left = Node(10)
sixteen.right = Node(21)
tree = BST(sixteen)

# Test Find
# print(tree.find(sixteen, 16))
# print(tree.find(sixteen, 10))
# print(tree.find(sixteen, 21))
# print(tree.find(sixteen, 15))

# Expected
# True
# True
# True
# False

# Actual
# True
# True
# True
# False

# Test Insert -- i did this kinda janky where I just print what node we are 
# recursing thru so i know where it inserts
# tree.insert(sixteen, 15) #insert on left
# should print 16, 10
# tree.insert(sixteen, 150) #insert on right
# should print 16, 21

