# Implement a Singly Linked List class with the following methods:

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None  # cons, we make a space tradeoff for quicker runtime


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
            new_node.prev = self.tail  # 4<-5
            self.tail.next = new_node  # ->3->4->5
            self.tail = new_node
        # print("increase size")
        self.len += 1
        print(self.len)

    # <Node> pop() → Removes the last node at the end of the linked list, returns that data
    # okay at this point, I decided that I wanted a doubly linked list for O(1) pop instead of O(n)
    def pop(self):
        self.len -= 1
        if self.isEmpty():
            self.len = 0
            return None
        return_node = self.tail
        if self.size == 1:
            self.head = None
            self.tail = None
        else:  # 1 -> 2 becomes 1
            new_tail = return_node.prev
            new_tail.next = None
            return_node.prev = None
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
        if self.len == 0:
            self.push(node)
        elif idx <= 0:  # for edge cases: if idx < 0, then insert at front
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            self.len += 1
        elif idx >= self.len - 1:  # if idx > 0 then insert at back
            self.push(node)
        else:  # 1 -> (2) new_node -> 3
            node3 = self.elementAt(idx)
            node1 = node3.prev
            node1.next = new_node
            new_node.prev = node1
            node3.prev = new_node
            new_node.next = node3
            self.len += 1

    # void remove(uint index) → remove/delete a single node at the index location in the list. If the node doesn’t exist at the index, do nothing
    def remove(self, idx):
        if idx >= self.len or idx < 0:
            return
        if self.len == 1:
            self.head = None
        elif idx == 0:
            new_head = self.head.next
            new_head.prev = None
            self.head.next = None
            self.head = new_head
        elif idx == self.len - 1:
            new_tail = self.tail.prev
            new_tail.next = None
            self.tail.prev = None
            self.tail = new_tail
        else:  # this case basically means there are atleast 3 elements. we need to free 4 pointers and delete the middle node
            to_del = self.elementAt(idx)  # 1 -> to_del -> 3
            node1 = to_del.prev
            node3 = to_del.next
            node1.next = node3
            node3.prev = node1
            to_del.prev = None
            to_del.next = None
            to_del = None
        self.len -= 1

    # <Node> elementAt(uint index) → Returns a pointer to the node at the index location in the list. If the node doesn’t exist at the index, return nil/null
    # approach: if the point is closer to head, iterate from the head to point; if the point is closer to the tail, iterate from the tail.
    # takes o(n/2) time worst case
    # if len = 5 and idx = 3:
    #   if len - idx < idx: go from tail
    #   else: go from the head
    def elementAt(self, idx):
        if idx == 0:
            return self.head
        elif idx == self.len - 1:
            return self.tail
        elif idx < 0:
            return None
        elif idx > self.len:
            return None

        if (self.len - idx) < idx:  # go from tail
            curr_node = self.tail.prev
            ctr = self.len - 3
            while curr_node != None:
                if ctr == idx:
                    return curr_node
                idx -= 1
                curr_node = curr_node.prev
        else:  # go from head
            curr_node = self.head.next
            ctr = 1
            while curr_node != None:
                if ctr == idx:
                    return curr_node
                idx += 1
                curr_node = curr_node.next

    # uint size() → Returns the length of the list.
    def size(self):
        return self.len
    # void printList() → Returns a string representation of the linked list
    # format I'm gonna use: 1 -> 2 -> ...

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
