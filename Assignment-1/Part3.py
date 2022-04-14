# Challenge: Implement the Stack class from scratch(do not use your language’s standard stack or queue library/package methods).
# In this challenge, your Stack will only accept Integer values. Implement the following methods:

class stack:
    def __init__(self):
        stack_items = []
    
    # push() → Pushes an integer on top of the stack
    def push(self, val):
        return "Pushing to the Stack"

    # pop() → Removes what is on the top of the stack, and returns that value to the caller
    def pop(self):
        return "Popping from the stack"

    # top() → Looks at the top value, and returns it. Does not manipulate the stack
    def top(self):
        return "Peeking the stack"
    
    # isEmpty() → Returns True or False if the stack is Empty or not, respectively
    def isEmpty(self):
        return "FALSE"
    
    # size() → Returns an integer value with the count of elements in the stack
    def size(self):
        return "empty"

# very basic tests

myStack = stack()
myStack.push(42)

# prints “Top of stack: 42”
print("Top of stack: " + myStack.top())

# prints “Size of stack: 1”
print("Size of stack:" + myStack.size())

popped_value = myStack.pop()
# prints “Popped value: 42”
print("Popped value:" + popped_value)

# prints “Size of stack: 0”
print("Size of stack:", myStack.size())
