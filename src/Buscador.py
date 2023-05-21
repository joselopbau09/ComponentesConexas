
import random 
from Graph import *


class Buscador:


    def __init__(self,graph):
        self.cola = []
        self.listaVertices = graph.getVertices()
        self.componentesConexas = []

    def bfs(self):
        while len(self.listaVertices) != 0:
            componeteConexa = []
            vertice = self.seleccionaVertice()
            self.cola.append(vertice)
            vertice.setVisitado()
            while len(self.cola) != 0:
                verticeAux = self.cola.pop(0)
                vecinos = verticeAux.getAdyacentes()
                for vecino in vecinos:
                    if not vecino.visitado:
                        self.cola.append(vecino)
                        vecino.setVisitado()
                    continue    
                componeteConexa.append(verticeAux.valor)
                self.listaVertices.remove(verticeAux)
            self.componentesConexas.append(componeteConexa)                                                                                                                                                       

    def seleccionaVertice(self) -> Vertice:
        if len(self.listaVertices) == 0:
            return -1
        return random.choice(self.listaVertices)

    def imprimeComponentes(self):
        cadena = ''
        for componente  in self.componentesConexas:
            cadena += '['
            for vertice in componente:
                cadena += f'{vertice}, '
            cadena += ']'    
        print(cadena)