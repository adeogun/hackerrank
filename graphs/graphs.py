import queue

class Graph:
    v = 0
    e = 0
    def __init__(self, V):
        self.v = V
        self.adj =  [[] for _ in range(V)]

    def addEdge(self,V, W ):
        self.adj[V].append(W)
        self.adj[W].append(V)
        self.e = self.e + 2

    def V(self):
        return self.v

    def E(self):
        return self.e

class DFSClass:

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

class CCClass:

    marked = []
    id = []
    count = 0

    def __init__(self, graph):
        self.marked = [False] * graph.V()
        self.id = [None] * graph.V()
        idd = 0

        for a in range(graph.V()):
            if self.marked[a] == False:
                self.id[a] = idd
                self.cc(graph, a, idd)
                idd = idd + 1
                self.count = self.count + 1

    def Count(self):
        return self.count


    def cc(self, graph, s, idd):
        self.marked[s] = True
        for v in graph.adj[s]:
            if self.marked[v] == False:
                self.id[v] = idd
                self.cc(graph, v, idd)


class BFSClass:

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
#
# CONNECTED COMPONENTS ccc = CCClass(g)