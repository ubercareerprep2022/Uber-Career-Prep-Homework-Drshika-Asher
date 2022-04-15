# Implement a Queue class from scratch that handles integers, with the following methods:
#
# implementing queue using a singly linked list. 
#
# some edge cases I was considering is making sure that my class works for multiple queue instances; 
# removing more than you add; isempty, enqueue, dequeue, rear, front, size on an on an empty queue
#
# this is better for us because enqueue is O(1) instead of O(1) amortized (with lists)


class Node:
    def __init__(self, data):
       self.data = data
       self.next = None 

class queue:
    def __init__(self):
        self.top = None
        self.back = None
        self.queue_size = 0

    # isEmpty() → returns whether or not the queue is empty
    def isEmpty(self):
        if self.queue_size == 0:
            return True
        else:
            return False

    def pprint(self): #made a pretty printer for debugging
        if self.isEmpty():
            return "Queue is empty"
        to_print = "[ "
        curr_node = self.top
        while curr_node != None:
            to_print += str(curr_node.data) + " "
            curr_node = curr_node.next  
        return to_print + "]"

    # enqueue() → adds an item to the queue
    def enqueue(self, item):
        new_node = Node(item)
        if self.isEmpty():
            self.top = new_node
            self.back = new_node
        else:  
            self.back.next = new_node
            self.back = self.back.next
        self.queue_size += 1

    # dequeue() → removes an item from the queue
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        to_return = self.top.data
        self.top = self.top.next
        self.queue_size -= 1
        return to_return

    # rear() → returns the item at the end of the queue
    def rear(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.back.data
    # front() → returns the item at the front of the queue
    def front(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.top.data   

    # size() → returns the size of the queue
    def size(self):
        if self.isEmpty():
            return "Queue is Empty"
        return self.queue_size

# Basic Tests
myQueue = queue()

# prints "FALSE"
print(myQueue.isEmpty())

myQueue.enqueue("Person 1")
myQueue.enqueue("Person 2")
myQueue.enqueue("Person 3")
myQueue.enqueue("Person 4")

print(myQueue.pprint())

# prints "Size of Queue: 4"
print("Size of Queue: " + str(myQueue.size()))

# prints "Front: Person 1"
print("Front: " + str(myQueue.front()))

# prints "Rear: Person 4"
print("Rear: " + str(myQueue.rear()))

# handle errors gracefully
myQueue.dequeue()
myQueue.dequeue()
myQueue.dequeue()
myQueue.dequeue()
print(myQueue.dequeue())

# prints "TRUE"
print(myQueue.isEmpty())

##########################
#   LIST IMPLEMENTATION  #
##########################

# class queue:
#     def __init__(self):
#         # do nothing
#         self.queue_items = []

#     # isEmpty() → returns whether or not the queue is empty
#     def isEmpty(self):
#         if self.queue_items:
#             return False
#         else:
#             return True

#     # enqueue() → adds an item to the queue
#     def enqueue(self, item):
#         self.queue_items = self.queue_items + [item]

#     # dequeue() → removes an item from the queue
#     def dequeue(self):
#         if self.isEmpty():
#             return "Queue is Empty"
#         self.queue_items = self.queue_items[1::]

#     # rear() → returns the item at the end of the queue
#     def rear(self):
#         if self.isEmpty():
#             return "Queue is Empty"
#         return self.queue_items[-1]

#     # front() → returns the item at the front of the queue
#     def front(self):
#         if self.isEmpty():
#             return "Queue is Empty"
#         return self.queue_items[0]

#     # size() → returns the size of the queue
#     def size(self):
#         if self.isEmpty():
#             return "Queue is Empty"
#         return len(self.queue_items)