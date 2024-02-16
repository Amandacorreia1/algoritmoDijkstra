import sys

class Grafo:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.grafo = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

    def exibir_solucao(self, distancias):
        print("\nDistância do vértice até a origem")
        for vertice in range(self.num_vertices):
            print("O vertice:", vertice, "menor distancia:", distancias[vertice])

    def menor_distancia(self, distancias, visitados):
        minima = sys.maxsize
        for v in range(self.num_vertices):
            if distancias[v] < minima and not visitados[v]:
                minima = distancias[v]
                indice_minimo = v
        return indice_minimo

    def dijkstra(self, origem):
        distancias = [sys.maxsize] * self.num_vertices
        distancias[origem] = 0
        visitados = [False] * self.num_vertices

        vertices_restantes = self.num_vertices
        while vertices_restantes > 0:
            u = self.menor_distancia(distancias, visitados)
            visitados[u] = True
            vertices_restantes -= 1

            for v in range(self.num_vertices):
                if (self.grafo[u][v] > 0 and
                    not visitados[v] and
                    distancias[v] > distancias[u] + self.grafo[u][v]):
                    distancias[v] = distancias[u] + self.grafo[u][v]
                   

        self.exibir_solucao(distancias)

g = Grafo(5)
g.grafo = [
    [0, 7, 0, 2, 0],
    [7, 0, 6, 0, 0],
    [0, 6, 0, 1, 4],
    [2, 0, 1, 0, 8],
    [0, 0, 4, 8, 0]
]

print("Iniciando o algoritmo de Dijkstra...\n")
g.dijkstra(0)

