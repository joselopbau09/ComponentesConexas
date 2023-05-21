
from sys import argv
from Graph import Graph

class LectorArchivo:  

    def __init__(self,nombreArchivo) -> None:
        self.nombreArchivo = nombreArchivo
        self.grafica = Graph()
        self.lecturaArchivo

    def lecturaArchivo(self) -> Graph:
        listaLineas = []
        with open(self.nombreArchivo) as archivo:
            listaLineas = archivo.readlines()
        self.grafica = self.creacionGrafica(listaLineas.pop(0))
        return self.unirVertices(listaLineas)

    def creacionGrafica(self,cadena):
        listaVertices  = cadena.split(',')
        eliminarSalto = listaVertices[len(listaVertices) - 1].replace('\n','')
        listaVertices[len(listaVertices) - 1] = eliminarSalto
        for vertice in listaVertices:
            self.grafica.addVertex(vertice)
                
    def unirVertices(self, listaCadenas):
        for cadena in listaCadenas:
            listaAristas  = cadena.split(',')
            eliminarSalto = listaAristas[1].replace('\n','')
            listaAristas[1] = eliminarSalto
            self.grafica.addEdge(listaAristas[0], listaAristas[1])
    
    def getGrafica(self):
        
        return self.grafica