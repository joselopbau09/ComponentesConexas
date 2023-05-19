
import random 
from Graph import *

class Buscador:
    
    def __init__(self,graph):
        self.cola = []
        self.listaVertices = graph.getVertices()
        self.componentesConexas = []

    def bfs(self):
        while self.listaVertices:
            componeteConexa = []
            vertice = self.seleccionaVertice
            self.cola.append(vertice)
            vertice.setVisited()
            while self.cola:
                verticeAux = self.cola.pop(0)
                vecinos = verticeAux.getConnection()
                for vecino in vecinos:
                    vecino.setVisited()
                componeteConexa.append(verticeAux.id)
                self.listaVertices.remove(verticeAux)
            self.componentesConexas.append(componeteConexa)                                                                                                                                                       

    def seleccionaVertice(self) -> Vertice:
        if len(self.listaVertices) == 0:
            return -1
        return random.choice(self.listaVertices)

    def imprimeConjuntoInd(self):
        cadena = ''
        for componente  in self.componentesConexas:
            cadena += '['
            for vertice in componente:
                cadena += f'{vertice.id}, '
            cadena += ']'    
        print(cadena)