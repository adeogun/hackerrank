import queue

class DiGraph:
    v = 0
    e = 0
    def __init__(self, V):
        self.v = V
        self.adj =  [[] for _ in range(V)]

    def add_edge(self,V, W ):
        self.adj[V].append(W)
        self.e = self.e + 1

    def V(self):
        return self.v

    def E(self):
        return self.e

class DFSClass:
    marked = []
    edge_to = []

    def __init__(self, s, graph):
        self.marked = [False] * graph.V()
        self.edge_to = [None] * graph.V()
        self.dfs(graph, s)

    def dfs(self, graph, s):
        self.marked[s] = True

        for v in graph.adj[s]:
            if self.marked[v] == False:
                self.edge_to[v] = s
                self.dfs(graph, v)

class BFSClass:
    marked = []
    dist_to = []

    def __init__(self, graph):
        self.marked = [False] * graph.V()
        self.dist_to = [None] * graph.V()
        self.bfs(graph)

    def bfs(self, graph):
        s = 0
        q = queue.Queue()
        q.put(s)
        dist = 1
        self.marked[0] = True
        self.dist_to[0] = 0

        for a in range(graph.V()):
            while q.empty() == False:
                s = q.get()
                for v in graph.adj[s]:
                    if self.marked[v] == False:
                        self.dist_to[v] = self.dist_to[s] + 1
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


