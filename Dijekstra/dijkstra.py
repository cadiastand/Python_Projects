class CQueue:
    def __init__(self):
        self.dqueue = list()

    def pop_front(self):
        self.dqueue.pop(0)

    def front(self):
        return self.dqueue[0]

    def push_back(self, value):
        self.dqueue.append(value)

    def empty(self) -> bool:
        return len(self.dqueue) == 0


class Edge:
    def __init__(self, source_, target_, weight_):
        self.source = source_
        self.target = target_
        self.weight = weight_


class Vertex:
    def __init__(self, id_, name_):
        self.id = id_
        self.name = name_
        self.edges = []
        self.minDistance = float('inf')
        self.previousVertex = None


    def addEdge(self, edge: Edge):
        self.edges.append(edge)


    def getEdges(self):
        return self.edges



class Dijkstra:
    def __init__(self):
        self.vertexes = list()

    def update_in_all_edges(self, vertex : Vertex) -> bool:
        update : bool = False
        for edge in vertex.getEdges():
            target : Vertex = self.vertexes[edge.target]
            new_weight = vertex.minDistance + edge.weight
            if new_weight < target.minDistance:
                target.minDistance = new_weight
                target.previousVertex = vertex
                update = True
        return update


    def computePath(self, sourceId):
        queue = CQueue()
        queue.push_back(self.vertexes[sourceId])
        closed = set()
        self.vertexes[sourceId].minDistance = 0

        while not queue.empty():
            vertex = queue.front()
            queue.pop_front()
            if vertex not in closed:
                for edge in vertex.getEdges():
                    target_vertex = self.vertexes[edge.target]
                    queue.push_back(target_vertex)
                    new_weight = vertex.minDistance + edge.weight
                    if target_vertex.minDistance > new_weight:
                        target_vertex.minDistance = new_weight
                        target_vertex.previousVertex = vertex
                closed.add(vertex)

        vertex_iterator : int = 0
        while vertex_iterator != len(self.vertexes):
            update : bool = self.update_in_all_edges(self.vertexes[vertex_iterator])
            if update is True:
                vertex_iterator = 0
            else:
                vertex_iterator += 1

    def getShortestPathTo(self, targetId) -> list:
        path = []
        current = self.vertexes[targetId]
        while current is not None:
            path.append(current)
            current = current.previousVertex
        return list(reversed(path))


    def createGraph(self, vertexes, edgesToVertexes):
        for vertex in vertexes:
            self.vertexes.append(vertex)

        for edge in edgesToVertexes:
            self.vertexes[edge.source].addEdge(edge)


    def resetDijkstra(self):
        for vertex in self.vertexes:
            vertex.minDistance = float('inf')
            vertex.previousVertex = None


    def getVertexes(self):
        return self.vertexes
