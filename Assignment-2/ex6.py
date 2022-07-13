import re
import time

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
            self.size +=1
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

def initbook():
    book = None;
    with open("data.csv", "r") as f:
        lines = f.readlines()
        for line in lines:
            vals = re.split(",", line)
            vals[1] = vals[1][0:9]
            if book is None:
                entry = PhoneBookEntry(vals[0], vals[1])
                book = PhoneBook(entry)
            else:
                book.insert(book.root, vals[0], vals[1])
    return book

def findbook(book):
    numtimes = 0
    with open("search.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            numtimes+=1
            book.find(book.root, line)
    return numtimes

tic = time.perf_counter()        
book = initbook()
toc = time.perf_counter()
size_book = book.size

blick = time.perf_counter() 
calls = findbook(book)
block = time.perf_counter()

print(f"Insert took {toc - tic:0.4f} seconds")
print(f"The size of the phone book is {size_book}")
print(f"find() was called {calls} times")
print(f"Find took {block-blick:0.4f} seconds")

# OUTPUT -- List implementation
# Insert took 1.8737 seconds
# The size of the phone book is 1000000
# find() was called 1000 times
# Find took -52.8955 seconds      

# OUTPUT -- BST implementation 
# Insert took 1.4572 seconds
# The size of the phone book is 1000000
# find() was called 1000 times
# Find took 0.0022 seconds