# Implement a Singly Linked List class with the following methods:

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    # making a helper to see if the LinkedList is empty
    def isEmpty(self):
        return True if self.len == 0 else False

    # void push(<Node> node) → Adds the node to the end of the list
    def push(self, val):
        new_node = Node(val)
        if self.isEmpty():  # None->3->None
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node  # tail -> new_node
            self.tail = new_node  # -> new_node (tail)
        self.len += 1

    # <Node> elementAt(uint index) → Returns a pointer to the node at the index location in the list. If the node doesn’t exist at the index, return nil/null
    # approach: walk to idx in the list and return elem. takes O(n) time
    def elementAt(self, idx):
        # base cases
        if idx == 0:
            return self.head
        elif idx == self.len - 1:
            return self.tail
        elif idx < 0:
            return None
        elif idx > self.len:
            return None

        curr = self.head
        ctr = 0
        while curr:  # walking the linked list
            if ctr == idx:
                return curr
            curr = curr.next
            ctr += 1

    # uint size() → Returns the length of the list.
    def size(self):
        return self.len

    # <Node> pop() → Removes the last node at the end of the linked list, returns that data
    def pop(self):
        if self.isEmpty():  # can't remove nothing
            self.len = 0
            return None
        if self.size == 1:  # 4  = pop() = None
            self.head = None
            self.tail = None
        else:  # at least 2 elements
            return_node = self.tail
            new_tail = self.elementAt(self.len - 2)
            new_tail.next = None  # removing the pointer to the tail
            self.tail = new_tail
            return return_node

    # void insert(uint index,<Node> node) → Adds a single node containing data to a chosen location in the list. If the index is above the size of the list, do nothing
    # assuming these are 0 indexed
    # before -> insert -> after
    # 3 cases
    # insert at head or tail
    # insert in the middle of the list
    def insert(self, idx, node):
        new_node = Node(node)
        if self.isEmpty():
            self.push(new_node)
        elif idx <= 0:  # for edge cases: if idx < 0, then insert at front
            new_node.next = self.head
            self.head = new_node
        elif idx >= self.len - 1:  # if idx > 0 then insert at back
            self.push(new_node)
        else:  # 1 -> (2) new_node -> 3
            node1 = self.elementAt(idx - 1)
            node3 = node1.next
            node1.next = new_node
            new_node.next = node3
            self.len += 1

    # void remove(uint index) → remove/delete a single node at the index location in the list. If the node doesn’t exist at the index, do nothing
    def remove(self, idx):
        if idx >= self.len or idx < 0:
            return
        elif idx == 0:
            self.head = self.head.next  # remove pointer to old node
        elif idx == self.len - 1:
            self.pop()
        else:  # this case basically means there are at least 3 elements. we need to free 2 pointers and delete the middle node
            node1 = self.elementAt(idx - 1)  # 1 -> to_del -> 3
            to_delete = node1.next
            node3 = to_delete.next
            node1.next = node3
            to_delete.next = None
        self.len -= 1

    # pretty printing for debugging
    def printList(self):
        if self.isEmpty():
            return ""
        curr_node = self.head
        p_list = ""
        while curr_node != None:
            p_list += str(curr_node.data) + " -> "
            curr_node = curr_node.next
        # removing the last 4 characters for the last arrow
        p_list = p_list[:-4]
        return p_list

# full disclosure, I did some googling to brush up on pytest
# to run the tests type the following in your terminal: `pytest Part4.py`

# Implement the following tests (should be self explanatory):


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
        my_list.pop()
        assert my_list.printList() == "11 -> 45"

    # # no test was mentioned for insert. i think i'll write one for that as well
    def test_insert(self):
        my_list = LinkedList()
        my_list.insert(4, 5)
        print(my_list.printList())
        assert my_list.printList() == "5", "List should handle insert when list is empty"

        my_list.insert(1, 7)
        assert my_list.printList() == "5 -> 7", "List should handle insert at end"

        my_list.insert(0, 3)
        assert my_list.printList() == "3 -> 5 -> 7", "List should handle insert at beginning"

        my_list.insert(1, 45)
        assert my_list.printList() == "3 -> 45 -> 5 -> 7", "List should insert in the middle"

    def test_remove(self):
        my_list = LinkedList()
        my_list.push(11)
        my_list.push(45)
        my_list.push(3)

        # to verify that I'm removing stuff correctly (also for pop and insert) I'll be using the print to test the values in the list.
        # testEraseRemovesCorrectNode
        my_list.remove(1)
        assert my_list.printList() == "11 -> 3", "List should handle remove in middle"

        my_list.remove(0)
        assert my_list.printList() == "3", "List should handle at start"

        my_list.push(11)
        my_list.remove(1)
        assert my_list.printList() == "3", "List should handle removing at end"
        # testEraseDoesNothingIfNoNode
        my_list.remove(35)
        assert my_list.printList() == "3", "Remove should not erase something out of bounds"

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

        # size update on insert
        my_list.insert(1, 1)
        assert my_list.size() == 3, "Your list should have 3 elements: 11->1->45"

        # size update on remove
        my_list.remove(1)
        assert my_list.size() == 2, "Your list should have 2 elements: 11->45"
