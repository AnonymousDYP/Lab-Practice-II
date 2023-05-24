# Program to print DFS traversal from a given given graph 
from collections import defaultdict 

# This class represents a directed graph using adjacency list representation 
class Graph: 
    # Constructor 
    def __init__(self): 
        # default dictionary to store graph 
        self.graph = defaultdict(list) 
    
    # function to add an edge to graph 
    def addEdge(self, u, v): 
        self.graph[u].append(v) 
    
    # A function used by DFS 
    def DFSUtil(self, v, visited): 
        # Mark the current node as visited and print it 
        visited.add(v) 
        print(v, end=' ') 
        # Recur for all the vertices adjacent to this vertex 
        for neighbour in self.graph[v]: 
            if neighbour not in visited: 
                self.DFSUtil(neighbour, visited) 

    # The function to do DFS traversal. It uses recursive DFSUtil() 
    def DFS(self, v): 
        # Create a set to store visited vertices 
        visited = set() 
        # Call the recursive helper function 
        # to print DFS traversal 
        self.DFSUtil(v, visited) 
# Driver code 
# Create a graph given in the above diagram
g = Graph() 

count = int(input("Enter the number of edges : "))

for i in range(0,count):
    print(f"\nEdge {i}")
    n1 = int(input("Enter node number 1 : "))
    n2 = int(input("Enter node number 2 : "))
    g.addEdge(n1, n2)

# g.addEdge(0, 1) 
# g.addEdge(0, 2) 
# g.addEdge(1, 2) 
# g.addEdge(2, 0) 
# g.addEdge(2, 3) 
# g.addEdge(3, 3) 

start = int(input("Enter starting node number : "))
print(f"Following is DFS from (starting from vertex {start})") 
g.DFS(start) 