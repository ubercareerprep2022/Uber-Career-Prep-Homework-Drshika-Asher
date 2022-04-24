# Implement reverseLinkedList() which takes in a linked list and returns a new linked list with the same elements in reverse order. For example, if the representation of your Linked List is “1, 2, 3, 4”, then reversing it would return “4, 3, 2, 1”.
# We have identified three main methodologies for achieving this solution, and we want to challenge you to build all three:
# (1) Iteratively
# In this context, “iteratively” means “looping through the data set”. Therefore, our solution should have a time complexity of O(n) and a space complexity of O(1).

# (2) Using a stack
# Leaning on our knowledge of stacks, can you think of a way to utilize a stack to solve this problem with a time complexity of O(n)?

# (3) Recursively
# Read up on recursion, and then apply that knowledge to come up with another version of this algorithm.

# linked list Implementation (from part 4)
# I'm going to adapt this to be singly linked (and remove some of the fancy stuff) because I'm assuming that y'all want to see a non-trivial solution
# Because otherwise you can just set the head to be the tail and the tail to be the head in a doubly linked list and you're done
from audioop import reverse
import collections

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def isEmpty(self):
        return True if self.len == 0 else False

    def push(self, val):
        new_node = Node(val)
        if self.isEmpty():  # None->3->None
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node  # ->3->4->5
            self.tail = new_node
        self.len += 1

    def pop(self):
        if self.isEmpty():
            self.len = 0
            return None
        return_node = self.head 
        self.head = self.head.next
        self.len -= 1
        return return_node

    def elementAt(self, idx):
        if idx == 0:
            return self.head
        elif idx == self.len - 1:
            return self.tail
        elif idx < 0:
            return None
        elif idx > self.len:
            return None

        curr_node = self.head.next
        ctr = 1
        while curr_node != None:
            if ctr == idx:
                return curr_node
            idx += 1
            curr_node = curr_node.next

    def size(self):
        return self.len

    def printList(self):
        if self.isEmpty():
            return ""
        curr_node = self.head
        p_list = ""
        while curr_node != None:
            p_list += str(curr_node.data) + " -> "
            curr_node = curr_node.next
        p_list = p_list[:-4]
        return p_list

    def reverse_iter(self):
        # example: NONE -> (1 -> 2) -> 3
        # NONE <- (1 <- 2) -> 3
        # 1 <- (2 -> 3)
        # 1 <- (2 <- 3)
        # store the previous, current and next
        # (1) the pointer 1->2 needs to be changed to (2 -> 1)
        curr = self.head
        prev_elem = None
        while curr != None:
            next_elem = curr.next
            curr.next = prev_elem
            prev_elem = curr
            curr = next_elem

        self.head.next = None
        temp_tail = self.head
        self.head = self.tail
        self.tail = temp_tail

    def reverse_stack(self):
        stack = collections.deque()
        curr = self.head
        while curr.next:
            next_n = curr.next
            val = self.pop()
            stack.append(val)
            curr = next_n
        while stack:
            self.push(stack.pop().data)

    def reverse_recur(self, subhead, prev):
        # If head is empty or has reached the head end
        print(subhead)
        if subhead is None:
            return
        if subhead.next is None:
            self.head = subhead
        # Reverse the rest head
        self.reverse_recur(subhead.next, subhead)
        tmp = self.tail.next
        self.tail.next = prev
        if prev is not None:
            self.tail = prev
            self.tail.next = tmp


# running tests to make sure that everything is functional
class TestLinkedList():
    def test_reverse_iter(self):
        my_list = LinkedList()
        my_list.push(11)
        my_list.push(45)
        my_list.push(3)
        my_list.reverse_iter()
        assert my_list.printList() == "3 -> 45 -> 11", "List reverse iteratively works well"
    
    def test_reverse_stack(self):
        my_list = LinkedList()
        my_list.push(11)
        my_list.push(45)
        my_list.push(3)
        my_list.reverse_stack()
        assert my_list.printList() == "3 -> 45 -> 11", "List reverse w/stack works well"

    def test_reverse_recur(self):
        my_list = LinkedList()
        my_list.push(1)
        my_list.push(2)
        my_list.push(3)
        my_list.reverse_recur(my_list.head, None)
        assert my_list.printList() == "3 -> 2 -> 1", "List reverse recursively works well"

    # testPushBackAddsOneNode
    def test_push(self):
        my_list = LinkedList()
        my_list.push(11)
        my_list.push(45)
        my_list.push(3)
        print(my_list.printList())
        assert my_list.tail.data == 3, "The last in the linked list should be 3"

    # testPopBackRemovesCorrectNode
    def test_pop(self):
        my_list = LinkedList()
        my_list.push(11)
        my_list.push(45)
        my_list.push(3)
        print(my_list.printList())
        my_list.pop()
        print(my_list.printList())
        assert my_list.printList() == "45 -> 3"

    def test_elementAt(self):
        my_list = LinkedList()
        my_list.push(11)
        my_list.push(45)
        my_list.push(3)
        # testElementAtReturnNode
        assert my_list.elementAt(
            1).data == 45, "List: 11->45->3, 3rd element is 45."

        # testElementAtReturnsNoNodeIfIndexDoesNotExist
        assert my_list.elementAt(
            4) == None, "List: 11->45->3, no element at 4th node."
        assert my_list.elementAt(
            -1) == None, "List: 11->45->3, no element at -1th node."

    # testSizeReturnsCorrectSize
    # thought of all the functions that would need to update the size of the linkedlist
    # push, pop, insert and remove
    # just going to make sure that they are all updating correctly
    def test_size(self):
        # size update on push
        my_list = LinkedList()
        my_list.push(11)
        my_list.push(45)
        my_list.push(3)

        assert my_list.size() == 3, "Your list should have 3 elements: 11->45->3"

        # size update on pop
        my_list.pop()
        assert my_list.size() == 2, "Your list should have 2 elements: 11->45"
