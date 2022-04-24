import sys
# Challenge: Implement the Stack class from scratch(do not use your language’s standard stack or queue library/package methods).
# In this challenge, your Stack will only accept Integer values. Implement the following methods:

# basically i started with the approach of making the stack as an array and only add and delete from the front.
# some edge cases I was considering is making sure that my class works for multiple stack instances,
# removing more than you add, isempty on an empty stack, top, pop and min on an empty stack.

# okay now we do it again but with a singly linked list.
# this is better for us because push is O(1) instead of O(1) amortized (with lists)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class stack:
    def __init__(self):
        # space time complexity tradeoff for O(1) access for global min
        self.global_min = sys.maxsize
        self.head = None
        self.stack_size = 0
    # isEmpty() → Returns True or False if the stack is Empty or not, respectively

    def isEmpty(self):
        if self.stack_size == 0:
            return True
        else:
            return False

    def pprint(self):  # made a pretty printer for debugging
        to_print = "[ "
        curr_node = self.head
        while curr_node != None:
            to_print += str(curr_node.data) + " "
            curr_node = curr_node.next
        return to_print + "]"

    # # push() → Pushes an integer on top of the stack
    def push(self, val):
        if self.isEmpty():
            self.head = Node(val)
            self.global_min = self.head.data
        else:
            new_head = Node(val)
            new_head.next = self.head
            if (self.head.data > val):
                self.global_min = val
            self.head = new_head
        self.stack_size += 1
    # pop() → Removes what is on the top of the stack, and returns that value to the caller

    def pop(self):
        if self.isEmpty():
            return "Nothing to pop"
        to_return = self.head.data
        self.head = self.head.next
        self.stack_size -= 1
        return to_return
    # top() → Looks at the top value, and returns it. Does not manipulate the stack

    def top(self):
        if self.isEmpty():
            return "Nothing on top"
        return self.head.data
    # size() → Returns an integer value with the count of elements in the stack

    def size(self):
        if self.isEmpty():
            return "Nothing in stack"
        return self.stack_size
    # min() → Returns an integer value of the smallest element in the stack

    def min(self):
        if self.isEmpty():
            return "Nothing in stack"
        return self.global_min


myStack = stack()
myStack.push(42)
myStack.push(34)
myStack.push(11)

# print(myStack.pprint())

# # prints “Top of stack: 42”
# print("Top of stack: " + str(myStack.top()))

# # prints “Size of stack: 1”
# print("Size of stack:" + str(myStack.size()))

# popped_value = myStack.pop()  # testing popping off more than I have
# # popped_value = myStack.pop()
# # popped_value = myStack.pop()
# # popped_value = myStack.pop()

# print(myStack.pprint())

# # prints “Popped value: 42”
# print("Popped value:" + str(popped_value))

# # prints “Size of stack: 0”
# print("Size of stack:", str(myStack.size()))

# # prints "Min: 11"
# print("Min:", str(myStack.min()))

# class stack:
#     def __init__(self):
#         self.stack_items = []
#         self.global_min = sys.maxsize

#     # isEmpty() → Returns True or False if the stack is Empty or not, respectively
#     def isEmpty(self):
#         if self.stack_items:
#             return False
#         else:
#             return True

#     # push() → Pushes an integer on top of the stack
#     def push(self, val):
#         if not self.stack_items: # using this global min part that takes constant time in push to get O(1) min access
#             self.global_min = val
#         else:
#             if val < self.global_min:
#                 self.global_min = val
#         self.stack_items = [val] + self.stack_items
#         print(self.stack_items)

#     # pop() → Removes what is on the top of the stack, and returns that value to the caller
#     def pop(self):
#         if self.isEmpty():
#             return "nothing to pop"  # i'm assuming this is how we want to handle out of bound errors
#         top = self.stack_items[0]
#         self.stack_items = self.stack_items[1::]
#         return top

#     # top() → Looks at the top value, and returns it. Does not manipulate the stack
#     def top(self):
#         if self.isEmpty():
#             return "nothing on top"
#         return self.stack_items[0]

#     # size() → Returns an integer value with the count of elements in the stack
#     def size(self):
#         return len(self.stack_items)

#     def min(self):
#         return self.global_min

# very basic tests


# myStack = stack()
# stack2 = stack()
# myStack.push(42)
# myStack.push(34)
# myStack.push(11)
# stack2.push(237489)

# # prints “Top of stack: 42”
# print("Top of stack: " + str(myStack.top()))

# # prints “Size of stack: 1”
# print("Size of stack:" + str(myStack.size()))

# popped_value = myStack.pop()  # testing popping off more than I have
# # popped_value = myStack.pop()
# # popped_value = myStack.pop()
# # popped_value = myStack.pop()

# # prints “Popped value: 42”
# print("Popped value:" + str(popped_value))

# # prints “Size of stack: 0”
# print("Size of stack:", str(myStack.size()))
# print("Size of stack:", str(stack2.size()))

# # prints "Min: 11"
# print("Min:", str(myStack.min()))
