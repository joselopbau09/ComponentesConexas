
import random 
from classes.Graph import *


class Buscador:
    """Se encarga de la busqueda de las componentes conexas de la grafica.

    Attributes:
        cola (list[Vertice]): Almacena los vertices que se visitian a la hora de realizar BFS.
        
        listaVertices (list[Vertice]): Todos los vertices de la grafica.
        
        componentesConexas (list[list[str]]): Almacena las componenetes conexas que hay en la grafica.
    """

    def __init__(self,graph):
        self.cola = []
        self.listaVertices = graph.getVertices()
        self.componentesConexas = []
        self.aristasComponentesConexas = []

    def bfs(self) -> None:
        while len(self.listaVertices) != 0:
            componenteConexa = []
            vertice = self.seleccionaVertice()
            self.cola.append(vertice)
            vertice.setVisitado()
            aristaComponenteConexa = ''
            while len(self.cola) != 0:
                verticeAux = self.cola.pop(0)
                vecinos = verticeAux.getAdyacentes()
                for vecino in vecinos:
                    if not vecino.visitado:
                        aristaComponenteConexa += f'{verticeAux.valor}, {vecino.valor} \n' 
                        self.cola.append(vecino)
                        vecino.setVisitado()
                    continue    
                componenteConexa.append(verticeAux.valor)
                self.listaVertices.remove(verticeAux)
                
            self.aristasComponentesConexas.append(aristaComponenteConexa)
            self.componentesConexas.append(componenteConexa)                                                                                                                                                       

    def seleccionaVertice(self) -> Vertice:
        if len(self.listaVertices) == 0:
            return -1
        return random.choice(self.listaVertices)

    def imprimeComponentes(self) -> None:
        cadena = f'Numero de componentes: {len(self.componentesConexas)}\n'
        i = 0
        while i < len(self.componentesConexas):
            j = 0
            cadena += '['
            while j < len(self.componentesConexas[i]):
                if j == len(self.componentesConexas[i]) - 1:
                    cadena += f'{self.componentesConexas[i][j]}]\n'                    
                    cadena += f'Aristas: \n{self.aristasComponentesConexas[i]}'
                else:
                    cadena += f'{self.componentesConexas[i][j]} ,'
                j+=1
            i+=1    
        print(cadena) 