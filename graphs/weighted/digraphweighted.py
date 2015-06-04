import queue

class Edge:    
    """
    Weighted edge representation
    """
    def __init__(self, V, E, Weight):
        self.v = V
        self.e = E
        self.weight = Weight
    
    def __str__(self):
        return "Vertice {0} Edge {1} Weight {2}".format(self.v, self.e, self.weight)

class DiGraph:
    """
    Directed weighted graph
    """
    v = 0
    e = 0
    def __init__(self, V):
        self.v = V
        self.adj =  [[] for _ in range(V)]

    def addEdge(self,V, W, Weight ):
        edge = Edge(V, W, Weight)
        self.adj[V].append(edge)
        self.e = self.e + 1

    def V(self):
        return self.v

    def E(self):
        return self.e

class DFSClass:
    """
    Depth first search
    """
    marked = []
    edgeTo = []

    def __init__(self, s, graph):
        self.marked = [False] * graph.V()
        self.edgeTo = [None] * graph.V()
        self.dfs(graph, s)

    def dfs(self, graph, s):
        self.marked[s] = True

        for v in graph.adj[s]:
            v = v.e            
            if self.marked[v] == False:
                self.edgeTo[v] = s
                self.dfs(graph, v)

class BFSClass:
    """
    Breadth first search
    """
    marked = []
    distTo = []

    def __init__(self, graph):
        self.marked = [False] * graph.V()
        self.distTo = [None] * graph.V()
        self.bfs(graph)

    def bfs(self, graph):
        s = 0
        q = queue.Queue()
        q.put(s)
        dist = 1
        self.marked[0] = True
        self.distTo[0] = 0

        for a in range(graph.V()):
            while q.empty() == False:
                s = q.get()
                for v in graph.adj[s]:
                    v = v.e
                    if self.marked[v] == False:
                        self.distTo[v] = self.distTo[s] + 1
                        self.marked[v] = True
                        q.put(v)

#class MST:
    #code

#class ShortestPath:
    #code

class Topological:
    """
    Topological sort order
    """
    marked = []
    edgeTo = []
    stack = []
    
    def __init__(self, graph):
        self.marked = [False] * graph.V()
        self.edgeTo = [None] * graph.V()
        for i in range(0, graph.v):
            if(self.marked[i] == False):
                self.dfs(graph, i)

    def dfs(self, graph, s):
        self.marked[s] = True

        for v in graph.adj[s]:
            v = v.e
            print("V {0} E {1}".format(s, v))
            if self.marked[v] == False:
                self.edgeTo[v] = s
                self.dfs(graph, v)
                
        self.stack.append(s)

#### USAGE
# CREATE INPUT graphin = [[0, 1],[0, 5]]
# INSTANTIATE g = DiGraph(len(graphin))
# ADD EDGES for inp in graphin:
#      g.addEdge(inp[0], inp[1], weight)
# DFS SEARCH dfsearch = DFSClass(0, g)
#
# BFS SEARCH bfss = BFSClass(g)