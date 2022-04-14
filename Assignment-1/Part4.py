# Implement a Queue class from scratch that handles integers, with the following methods:

import sys


class queue:
    def __init__(self):
        # do nothing
        self.queue_items = []
        self.global_min = sys.maxsize

    # isEmpty() → returns whether or not the queue is empty
    def isEmpty(self):
        if self.queue_items:
            return False
        else:
            return True

    # enqueue() → adds an item to the queue
    def enqueue(self, item):
        self.queue_items = self.queue_items + [item]

    # dequeue() → removes an item from the queue
    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        self.queue_items = self.queue_items[1::]

    # rear() → returns the item at the end of the queue
    def rear(self):
        if self.isEmpty():
            return "Queue is Empty"
        return self.queue_items[-1]

    # front() → returns the item at the front of the queue
    def front(self):
        if self.isEmpty():
            return "Queue is Empty"
        return self.queue_items[0]

    # size() → returns the size of the queue
    def size(self):
        if self.isEmpty():
            return "Queue is Empty"
        return len(self.queue_items)


# Basic Tests
myQueue = queue()

# prints "FALSE"
print(myQueue.isEmpty())

myQueue.enqueue("Person 1")
myQueue.enqueue("Person 2")
myQueue.enqueue("Person 3")
myQueue.enqueue("Person 4")

# prints "Size of Queue: 4"
print("Size of Queue:" + str(myQueue.size()))

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
