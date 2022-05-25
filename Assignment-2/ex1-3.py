import re

# [Trees - Ex1] Exercise: Printing a tree
# Implement a method called print() to print the values of the data in all the TreeNodes in a Tree above. For example, running print() on the Tree above should produce one of the three values below:

# Okay so this immediately reminds me of traversals. I just chose one, (preorder)
# So recursively we have to process root, left then right
# Handling cases where the input is none to make sure the recursion breaks
# coming back to code the other options for fun :)

class TreeNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

class Tree:
    def __init__(self, root: TreeNode):
        self.root = root
    # doing a simple pre-order traversal
    def print_tree_preorder(self, subroot):
        if subroot == None:
            return ""
        else:
            return str(subroot.data) + " " + self.print_tree_preorder(subroot.left) + " " + self.print_tree_preorder(subroot.right)
    # inorder
    def print_tree_inorder(self, subroot):
        if subroot == None:
            return ""
        else:
            return self.print_tree_inorder(subroot.left) + " " + str(subroot.data) + " " + self.print_tree_inorder(subroot.right)
    # postorder
    def print_tree_postorder(self, subroot):
        if subroot == None:
            return ""
        else:
            return self.print_tree_postorder(subroot.left) + " " + self.print_tree_postorder(subroot.right) + " " + str(subroot.data)

#construct example tree
six = TreeNode(6, None, None)
three = TreeNode(3, None, None)
seven = TreeNode(7, None, None)
seventeen = TreeNode(17, six, three)
one = TreeNode(1, seven, seventeen)

ex = Tree(one)
empty_tree = Tree(None)
# print(ex.root.data)
pre = ex.print_tree_preorder(ex.root)
post = ex.print_tree_inorder(ex.root)
inorder = ex.print_tree_postorder(ex.root)
print(re.sub(" +", " ", pre)) #using regex to clean the output for extra spaces
print(re.sub(" +", " ", post))
print(re.sub(" +", " ", inorder))
print(empty_tree.print_tree_inorder(empty_tree.root))

# Expected Output:
# 1 7 17 6 3
# 7 1 6 17 3
# 7 6 3 17 1 
#

# Test Output:
# 1 7 17 6 3 
#  7 1 6 17 3 
#  7 6 3 17 1
#
