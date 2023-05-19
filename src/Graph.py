
import sys

class Vertice:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

        self.visted = False
        self.previous = None

    def addNeighbor(self, neighbor, weight = 0):    
        self.adjacent[neighbor] = weight

    def getConnection(self): 
        lista = []
        for vertice in list(self.adjacent.keys()):
            lista.append(self.adjacent[vertice])
        return lista

    def getverticeId(self):
        return self.id 

    def setPrevious(self, prev):
        self.previous = prev

    def setVisited(self):
        self.visted = True

    def getAdjacent(self):
        return self.adjacent

    def __str__(self):
        return f'{str(self.id)} adjacent: {str([x.id for x in self.adjacent])}'                    

class Graph:
    def __init__(self):
        self.vertDictionery = {}
        self.numVertices = 0

    def __iter__(self):
        return iter(self.vertDictionery.values())

    def addVertex(self ,node):
        self.numVertices += 1
        newVertex = Vertice(node)
        self.vertDictionery[node] = newVertex
        return newVertex

    def getVertex(self, n):     
        if n  in self.vertDictionery:
            return self.vertDictionery[n]
        else:
            return None

    def addEdge(self, frm, to, cost = 0):
        if frm not in self.vertDictionery:
            self.addVertex(frm)
        if to not in self.vertDictionery:
            self.addVertex(to)
        self.vertDictionery[frm].addNeighbor(self.vertDictionery[to], cost)

    def getVertices(self):
        lista = []
        for vertice in list(self.vertDictionery.keys()):
            lista.append(self.vertDictionery[vertice])
        return lista
        
    def getNumVertices(self):
        return self.numVertices

    def setPrevious(self,current):                                
        self.previous = current

    def getPrevious(self):                                
        return self.previous 

    def getEdges(self,graph):
        edges = []
        G = graph
        for v in G:
            for w in v.getConnection():
                vid = v.getverticeId()    
                wid = w.getverticeId()
                edges.append((vid, wid))
        return edges