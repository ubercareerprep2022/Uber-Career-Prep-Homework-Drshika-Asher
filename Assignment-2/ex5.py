# For the first implementation, which we will call ListPhoneBook, please use a List (specifically an ArrayList) as the underlying data structure to implement the methods. 

# For the second implementation, which we will call BinarySearchTreePhoneBook, please use a binary search tree as the underlying data structure to implement the methods.

# Interface for a phone book.
# Each entry in the phone book is made up of 2 components: a name (String) and a
# phone number (long).
# For the purposes of this exercise, you can assume that there are no duplicate names.

# LIST IMPLEMENTATION
# class PhoneBookEntry:
#     def __init__(self, name, number):
#         self.name = name
#         self.number = number

# class PhoneBook:
#     def __init__(self):
#         self.book = []
#     # @return The number of entries in this phone book.    
#     def size(self):
#         return len(self.book)

#     # Inserts an entry in this phone book.
#     # @param name The name for the entry.
#     # @param phoneNumber The phone number for the entry.
#     def insert(self, name, number):
#         entry = PhoneBookEntry(name, number)
#         self.book.append(entry)

#     # Returns the phone number associated with a name in the phone book.
#     # @param name The name to search for.
#     # @return The phone number for the entry, or -1 if the name is not present in the phone book.
#     def find(self, name):
#         for entry in self.book:
#             if entry.name == name:
#                 return entry.number
#         return -1

# Testing Part 1
# book = PhoneBook()
# book.insert("person1", 123)
# book.insert("person2", 456)
# book.insert("person3", 789)
# print(book.find("person1")) # returns 123
# print(book.find("person5")) # returns -1

class PhoneBookEntry:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.left = None
        self.right = None

# BINARY SEARCH TREE IMPL
class PhoneBook:
    def __init__(self):
        self.root = None
        self.size = 0
    def __init__(self, root):
        self.root = root
        self.size = 1
    def size(self):
        return self.size
    # Inserts an entry in this phone book.
    # @param name The name for the entry.
    # @param phoneNumber The phone number for the entry.
    def insert(self, subroot, name, number):
        if subroot is None:
            return PhoneBookEntry(name, number)
        else:
            if subroot.name < name:
                self.insert(subroot.left, name, number)
            elif subroot.name >= name:
                self.insert(subroot.right, name, number)
            return self.root
    def find(self, subroot, name):
        if subroot is None:
            return -1
        elif subroot.name is name:
            return subroot.number
        elif name < subroot.name:
            return self.find(subroot.left, name)
        elif name >= subroot.name:
            return self.find(subroot.right, name)
# Testing Part 2
entry1 = PhoneBookEntry("person1", 123)
book = PhoneBook(entry1)
book.insert(entry1, "person2", 456)
book.insert(entry1, "person3", 789)
print(book.find(entry1, "person1")) # returns 123
print(book.find(entry1, "person5")) # returns -1

# conclusions: find/insert in btree works better (avg case) than find in list impl since both take O(n) > O(h) time respectively