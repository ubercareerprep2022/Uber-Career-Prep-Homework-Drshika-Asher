# Challenge: Implement the Stack class from scratch(do not use your language’s standard stack or queue library/package methods).
# In this challenge, your Stack will only accept Integer values. Implement the following methods:

# okay so basically i wanted to make the stack as an array and only add and delete from the front. 
# some edge cases I was considering is making sure that my class works for multiple stack instances, 
# removing more than you add, isempty on an empty stack, top, pop and min on an empty stack.

import sys


class stack:
    def __init__(self):
        # do nothing
        self.stack_items = []
        self.global_min = sys.maxsize

    # isEmpty() → Returns True or False if the stack is Empty or not, respectively
    def isEmpty(self):
        False if not self.stack_items else True

    # push() → Pushes an integer on top of the stack
    def push(self, val):
        if not self.stack_items: # using this global min part that takes constant time in push to get O(1) min access
            self.global_min = val
        else:
            if val < self.global_min:
                self.global_min = val
        self.stack_items = [val] + self.stack_items
        print(self.stack_items)

    # pop() → Removes what is on the top of the stack, and returns that value to the caller
    def pop(self):
        if self.isEmpty():
            return "nothing to pop"  # i'm assuming this is how we want to handle out of bound errors
        top = self.stack_items[0]
        self.stack_items = self.stack_items[1::]
        return top

    # top() → Looks at the top value, and returns it. Does not manipulate the stack
    def top(self):
        if self.isEmpty():
            return "nothing on top"
        return self.stack_items[0]

    # size() → Returns an integer value with the count of elements in the stack
    def size(self):
        return len(self.stack_items)

    def min(self):
        return self.global_min

# very basic tests


myStack = stack()
stack2 = stack()
myStack.push(42)
myStack.push(34)
myStack.push(11)
stack2.push(237489)

# prints “Top of stack: 42”
print("Top of stack: " + str(myStack.top()))

# prints “Size of stack: 1”
print("Size of stack:" + str(myStack.size()))

popped_value = myStack.pop()  # testing popping off more than I have
# popped_value = myStack.pop()
# popped_value = myStack.pop()
# popped_value = myStack.pop()

# prints “Popped value: 42”
print("Popped value:" + str(popped_value))

# prints “Size of stack: 0”
print("Size of stack:", str(myStack.size()))
print("Size of stack:", str(stack2.size()))

# prints "Min: 11"
print("Min:", str(myStack.min()))
