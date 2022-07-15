# assumptions: graph is undirected
from collections import deque


class GraphNode:
    def __init__(self, data):
        self.data = data

class Graph:
    def __init__(self):
        self.graph = None # for this one, I'm going to use a map where key is graph node object, and the value is a list of graph node objects
    # Adds a new node to the graph.
    def addNode(self,key: int):
        if self.graph is None:
            self.graph = dict()
        new_node = GraphNode(key)
        self.graph[new_node] = []
    # making a helper to find node
    def findNode(self, key: int):
        for node in self.graph.keys():
            if node.data == key:
                return node
    # Removes the node from the graph. 
    def removeNode(self,key: int):
        #find the node
        n_node = self.findNode(key)
        #remove the node
        neighbors = self.graph.pop(n_node)
        #remove all edges between neighbors
        for neighbor in neighbors:
            val = self.graph[neighbor]
            if n_node in val:
                val.remove(n_node)
    # Adds an edge between node1 and node2
    def addEdge(self,node1: int, node2: int):
        #find node1
        n_node1 = self.findNode(node1)
        #find node2
        n_node2 = self.findNode(node2)
        #add edge to node1
        self.graph[n_node1].append(n_node2)
        #add edge to node2
        self.graph[n_node2].append(n_node1)

    # Removes an edge between node1 and node2. 
    def removeEdge(self,node1: int, node2: int):
        #find node1
        n_node1 = self.findNode(node1)
        #find node2
        n_node2 = self.findNode(node2)
        #add edge to node1
        self.graph[n_node1].remove(n_node2)
        #add edge to node2
        self.graph[n_node2].remove(n_node1)

    # Get nodes that are connected to the node represented by ‘key’
    def getAdjNodes(self,key: int):
        #find node
        n_node = self.findNode(key)
        return self.graph[n_node]
    
    #making a pretty printer for debugging
    def pprint(self):
        print_g = dict()
        for key in graph.graph: #initialize keys
            print_g[key.data] = []
            for value in graph.graph[key]:
                print_g[key.data].append(value.data)
        print(print_g)
    
    # Depth-First Traversal: A depth-first traversal starts at an arbitrary root node and explores nodes as deeper as possible along each branch
    def bfs(self, key:int):
        visited = set()
        queue = deque() # bfs barbeque
        s_node = self.findNode(key)
        queue.append(s_node)
        visited.add(s_node)
        while queue:
            s = queue.popleft()
            print(s.data, end = " ")

            for neighbor in graph.graph[s]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
            

    # Write a method to perform BFS(int key) traverses BFS  starting from key printing each node along the way. 
    def dfs(self, key:int):
        visited = set()
        stack = deque() # just same thing as bfs but with stack. i chose iterative impl but you could do with queue
        s_node = self.findNode(key)
        stack.append(s_node)
        visited.add(s_node)
        while stack:
            s = stack.pop()
            print(s.data, end = " ")

            for neighbor in graph.graph[s]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)


# TEST GRAPH CLASS
graph = Graph()
graph.addNode(1)
graph.addNode(2)
graph.addNode(3)
graph.addNode(4)
graph.addNode(5)
graph.addEdge(1,2)
graph.addEdge(1,3)
graph.addEdge(2,3)
graph.addEdge(2,5)
graph.addEdge(3,4)
graph.addEdge(4,5)

# # EXPECTED: {1: [2, 3], 2: [1, 3, 5], 3: [1, 2, 4], 4: [3, 5], 5: [2, 4]}
# graph.pprint()
# # ACTUAL: {1: [2, 3], 2: [1, 3, 5], 3: [1, 2, 4], 4: [3, 5], 5: [2, 4]}

# # EXPECTED: {2: [3, 5], 3: [2, 4], 4: [3, 5], 5: [2, 4]}
# graph.removeNode(1)
# graph.pprint()
# # ACTUAL: {2: [3, 5], 3: [2, 4], 4: [3, 5], 5: [2, 4]}

# # EXPECTED: {2: [5], 3: [4], 4: [3, 5], 5: [2, 4]}
# graph.removeEdge(2,3)
# graph.pprint()  
# # ACTUAL: {2: [5], 3: [4], 4: [3, 5], 5: [2, 4]}

# # TEST TRAVERSAL
# # EXPECTED: 1 2 3 5 4
# graph.bfs(1)
# # ACTUAL: 1 2 3 5 4

# # EXPECTED: 1 3 4 5 2
# graph.dfs(1)
# # ACTUAL: 1 3 4 5 2