
from sys import argv
from classes.Buscador import Buscador
from classes.Graph import Graph

def lecturaArchivo(nombre:str) -> Graph:
    """Se encarga de la lectura del archivo.

    Args:
        nombre (str): Direccion del archico a leer.

    Returns:
        Graph: Grafica creada. 
    """
    listaLineas = []
    with open(nombre) as archivo:
        listaLineas = archivo.readlines()
    grafica = creacionGrafica(listaLineas.pop(0))
    return unirVertices(listaLineas, grafica)

def creacionGrafica(cadena:str) -> Graph:
    """Realiza la creacion de la grafica.

    Args:
        cadena (str): Vertices de la grafica.

    Returns:
        Graph: Grafica creada. 
    """
    grafica = Graph()
    listaVertices  = cadena.split(',')
    eliminarSalto = listaVertices[len(listaVertices) - 1].replace('\n','')
    listaVertices[len(listaVertices) - 1] = eliminarSalto
    for vertice in listaVertices:
        grafica.agregarVertice(vertice)
            
    return grafica

def unirVertices(listaCadenas:list[str], grafica:Graph) -> Graph:
    """Se encarga de la conectar los vertices de la grafica.

    Args:
        listaCadenas (list[str]): Lista que almacena las aristas de la grafica.
        
        grafica (Graph): Grafica de la que se uniran los vertices.
    Returns:
        Graph: Grafica creada. 
    """
    graph = grafica
    for cadena in listaCadenas:
        listaAristas  = cadena.split(',')
        eliminarSalto = listaAristas[1].replace('\n','')
        listaAristas[1] = eliminarSalto
        graph.agregarArista(listaAristas[0], listaAristas[1])
    return graph    

def main():
    script, documento = argv
    nombreDocumento = "assets/%s"%documento
    grafica1 = lecturaArchivo(nombreDocumento)
    buscador = Buscador(grafica1)
    buscador.bfs()
    buscador.imprimeComponentes()
main()
