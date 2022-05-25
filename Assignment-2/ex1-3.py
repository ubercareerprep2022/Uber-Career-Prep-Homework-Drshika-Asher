import re
from collections import deque

# [Trees - Ex1] Exercise: Printing a tree
# Implement a method called print() to print the values of the data in all the TreeNodes in a Tree above. For example, running print() on the Tree above should produce one of the three values below:

# Okay so this immediately reminds me of traversals. I just chose one, (preorder)
# So recursively we have to process root, left then right
# Handling cases where the input is none to make sure the recursion breaks
# coming back to code the other options for fun :)

# [Trees - Ex2] Exercise: Printing a tree level by level
# Implement a method called printLevelByLevel() for the class OrganizationStructure that prints it level by level. For example, running printLevelByLevel() on the OrganizationStructure above should produce the following output:

# This is a level order traversal. So for this, we need to use a queue. I'm going to use the python dequeue library for this. The method is as follows: enqueue root, while queue is not empty, dequeue e, print(e), enqueue e.left & e.right

# [Trees - Ex3] Exercise: Printing the number of levels
# Implement a method called printNumLevels() for the class OrganizationStructure that prints the number of levels in it. For example, running printNumLevels() on the OrganizationStructure above should print 5. Running printNumLevels() on the OrganizationStructure below should print 4.

# Approach: Take level order traversal and modify it so that we add one every time we recurse down a level. Then take the max level height for left and right subtree. Instead of storing a node in the queue, we store a tuple of the height and the currr node. To modify this alg for an m-ary tree, we have to just take the max across all the children in the level.

# really barebones tree and treenode classes
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
    def print_level_order(self, subroot): #Runtime O(n) for all traversals
        queue = deque()
        queue.append(subroot)
        level = ""
        while queue:
            popped = queue.popleft()
            level += str(popped.data) + " "
            if not queue: # this is to get the formatting that the answer in the handout had (newline at each level)
                print(level)
                level = ""
            if popped.left != None: queue.append(popped.left) #add nullchecks that psuedocode didn't mention
            if popped.right != None: queue.append(popped.right)
    def num_levels(self, subroot): #runtime O(n)
        queue = deque()
        queue.append((subroot, 0))
        level = 0
        total = 0
        while queue:
            popped = queue.popleft()
            level = max(level, popped[1])
            total += 1
            if popped[0].left != None:
                queue.append((popped[0].left, popped[1] + 1))
            if popped[0].right != None:
                queue.append((popped[0].right, popped[1] + 1))
        return level + 1 #counting the head as a level

#construct example tree
six = TreeNode(6, None, None)
three = TreeNode(3, None, None)
seven = TreeNode(7, None, None)
seventeen = TreeNode(17, six, three)
one = TreeNode(1, seven, seventeen)

ex = Tree(one)
empty_tree = Tree(None)
# print(ex.root.data)

# TEST PART 1
# pre = ex.print_tree_preorder(ex.root)
# post = ex.print_tree_inorder(ex.root)
# inorder = ex.print_tree_postorder(ex.root)
# print(re.sub(" +", " ", pre)) #using regex to clean the output for extra spaces
# print(re.sub(" +", " ", post))
# print(re.sub(" +", " ", inorder))
# print(empty_tree.print_tree_inorder(empty_tree.root))

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

# TEST PART 2
# ex.print_level_order(ex.root)

# Expected Output:
# 1 
# 7 17 
# 6 3 

# Test Output
# 1 
# 7 17 
# 6 3 

# TEST PART 3
print(ex.num_levels(ex.root))

# Expected Output:
# 3

# Test Output: 
# 3