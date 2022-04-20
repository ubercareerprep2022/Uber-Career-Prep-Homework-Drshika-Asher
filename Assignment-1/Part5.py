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
        return_node = self.tail
        if self.size == 1:
            self.head = None
            self.tail = None
        else:  # 1 -> 2 becomes 1
            new_tail = self.elementAt(self.len-2)
            print(self.len)
            new_tail.next = None
            self.tail = new_tail
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
        # example: (1 <=> 2) <=> 3
        # there's two pointers to change the direction of.
        # (1) the pointer 1->2 needs to be changed to
        pass

    def reverse_stack(self):
        pass

    def reverse_recur(self):
        pass


# running tests to make sure that everything is functional
class TestLinkedList():
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
        assert my_list.printList() == "11 -> 45"

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
