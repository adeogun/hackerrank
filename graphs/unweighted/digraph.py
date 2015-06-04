import queue

class DiGraph:
    """
    Directed graph
    """
    v = 0
    e = 0
    def __init__(self, V):
        self.v = V
        self.adj =  [[] for _ in range(V)]

    def addEdge(self,V, W ):
        self.adj[V].append(W)
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
                    if self.marked[v] == False:
                        self.distTo[v] = self.distTo[s] + 1
                        self.marked[v] = True
                        q.put(v)

#### USAGE
# CREATE INPUT graphin = [[0, 1],[0, 5]]
# INSTANTIATE g = DiGraph(len(graphin))
# ADD EDGES for inp in graphin:
#      g.addEdge(inp[0], inp[1])
# DFS SEARCH dfsearch = DFSClass(0, g)
#
# BFS SEARCH bfss = BFSClass(g)

