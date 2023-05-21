
class Vertice:
    def __init__(self, node):
        self.valor = node
        self.adyacente = {}

        self.visitado = False
        self.anterior = None

    def agregarVecino(self, vecino, weight = 0):    
        self.adyacente[vecino] = weight

    def getVecinos(self):          
        return list(self.adyacente.keys())

    def getVerticeValor(self):
        return self.valor 

    def setAnterior(self, prev):
        self.anterior = prev
 
    def setVisitado(self):
        self.visitado = True

    def getAdyacentes(self):
        return list(self.adyacente.keys())

    def __str__(self):
        return f'{str(self.valor)} adyacente: {str([x.valor for x in self.adyacente])}'                    

class Graph:
    def __init__(self):
        self.diccionarioVertices = {}

    def __iter__(self):
        return iter(self.diccionarioVertices.values())

    def agregarVertice(self ,node):
        newVertice = Vertice(node)
        self.diccionarioVertices[node] = newVertice
        return newVertice

    def getVertice(self, n):     
        if n  in self.diccionarioVertices:
            return self.diccionarioVertices[n]
        else:
            return None

    def agregarArista(self, frm, to, cost = 0):
        if frm not in self.diccionarioVertices:
            self.agregarVertice(frm)
        if to not in self.diccionarioVertices:
            self.agregarVertice(to)
        self.diccionarioVertices[frm].agregarVecino(self.diccionarioVertices[to], cost)
        self.diccionarioVertices[to].agregarVecino(self.diccionarioVertices[frm], cost)

    def getVertices(self):
        lista = []
        for vertice in list(self.diccionarioVertices.keys()):
            lista.append(self.diccionarioVertices[vertice])
        return lista
