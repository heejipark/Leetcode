"""
There are two types of representations for a graph. 
1. Adjacency Matrix 
2. Adjacency List
"""

"""
1. Adjacency Matrix: 
Adjacency Matrix is a 2D array of size V x V where V is the number of vertices in a graph. 
Let the 2D array be adj[][], a slot adj[i][j] = 1 indicates that there is an edge from vertex i to vertex j. 
Adjacency matrix for undirected graph is always symmetric. Adjacency Matrix is also used to represent weighted graphs. 
If adj[i][j] = w, then there is an edge from vertex i to vertex j with weight w. 

# Adjacent Matrix
    0 1 2 3 4
    1 0 1 0 0
    2 1 0 0 0
    3 0 0 0 1
    4 0 0 1 0

Pros: Representation is easier to implement and follow. Removing an edge takes O(1) time.
      Queries like whether there is an edge from vertex ‘u’ to vertex ‘v’ are efficient and can be done O(1).
Cons: Consumes more space O(V^2). Even if the graph is sparse(contains less number of edges), it consumes the same space.
      Adding a vertex is O(V^2) time. Computing all neighbors of a vertex takes O(V) time (Not efficient).
"""
#A simple representation of graph using Adjacency Matrix
class Graph:
    def __init__(self,numvertex):
        self.adjMatrix = [[-1]*numvertex for x in range(numvertex)]
        self.numvertex = numvertex
        self.vertices = {}
        self.verticeslist =[0]*numvertex

    def set_vertex(self,vtx,id):
        if 0<=vtx<=self.numvertex:
            self.vertices[id] = vtx
            self.verticeslist[vtx] = id

    def set_edge(self,frm,to,cost=0):
        frm = self.vertices[frm]
        to = self.vertices[to]
        self.adjMatrix[frm][to] = cost
        #for directed graph do not add this
        self.adjMatrix[to][frm] = cost

    def get_vertex(self):
        return self.verticeslist

    def get_edges(self):
        edges=[]
        for i in range (self.numvertex):
            for j in range (self.numvertex):
                if (self.adjMatrix[i][j]!=-1):
                    edges.append((self.verticeslist[i],self.verticeslist[j],self.adjMatrix[i][j]))
        return edges
        
    def get_matrix(self):
        return self.adjMatrix

G =Graph(6)
G.set_vertex(0,'a')
G.set_vertex(1,'b')
G.set_vertex(2,'c')
G.set_vertex(3,'d')
G.set_vertex(4,'e')
G.set_vertex(5,'f')
G.set_edge('a','e',10)
G.set_edge('a','c',20)
G.set_edge('c','b',30)
G.set_edge('b','e',40)
G.set_edge('e','d',50)
G.set_edge('f','e',60)
print("Vertices of Graph")
print(G.get_vertex())
print("Edges of Graph")
print(G.get_edges())
print("Adjacency Matrix of Graph")
print(G.get_matrix())
#This code is contributed by Rajat Singhal

"""
2. Adjacency List: 
An array of lists is used. The size of the array is equal to the number of vertices. 
Let the array be an array[]. An entry array[i] represents the list of vertices adjacent to the ith vertex. 
This representation can also be used to represent a weighted graph. The weights of edges can be represented as lists of pairs.

# Adjacent List
0: [1]
1: [0, 2]
2: [1]
3: [4]
4: [3]

Pros: Saves space O(|V|+|E|). In the worst case, there can be C(V, 2) number of edges in a graph thus consuming O(V^2) space. 
      Adding a vertex is easier. Computing all neighbors of a vertex takes optimal time.
Cons: Queries like whether there is an edge from vertex u to vertex v are not efficient and can be done O(V).
      In Real-life problems, graphs are sparse(|E| <<|V|2). 
      That’s why adjacency lists Data structure is commonly used for storing graphs. 
      Adjacency matrix will enforce (|V|2) bound on time complexity for such algorithms. 

"""

# A class to represent the adjacency list of the node
class AdjNode:
	def __init__(self, data):
		self.vertex = data
		self.next = None

# A class to represent a graph. A graph
# is the list of the adjacency lists.
# Size of the array will be the no. of the
# vertices "V"
class Graph:
	def __init__(self, vertices):
		self.V = vertices
		self.graph = [None] * self.V

	# Function to add an edge in an undirected graph
	def add_edge(self, src, dest):
		# Adding the node to the source node
		node = AdjNode(dest)
		node.next = self.graph[src]
		self.graph[src] = node

		# Adding the source node to the destination as
		# it is the undirected graph
		node = AdjNode(src)
		node.next = self.graph[dest]
		self.graph[dest] = node

	# Function to print the graph
	def print_graph(self):
		for i in range(self.V):
			print("Adjacency list of vertex {}\n head".format(i), end="")
			temp = self.graph[i]
			while temp:
				print(" -> {}".format(temp.vertex), end="")
				temp = temp.next
			print(" \n")


# Driver program to the above graph class
if __name__ == "__main__":
	V = 5
	graph = Graph(V)
	graph.add_edge(0, 1)
	graph.add_edge(0, 4)
	graph.add_edge(1, 2)
	graph.add_edge(1, 3)
	graph.add_edge(1, 4)
	graph.add_edge(2, 3)
	graph.add_edge(3, 4)

	graph.print_graph()

# This code is contributed by Kanav Malhotra
# Reference: https://www.geeksforgeeks.org/graph-and-its-representations/
