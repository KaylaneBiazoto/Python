import random
from collections import deque

g = {
    1: [2, 3, 4], 
    2: [1, 3], 
    3: [1, 2], 
    4: [1, 5], 
    5: [4]
}

n = 5
d = {}


def dfs(u, g, visited_edge, path = []):

    path = path + [u]

    for v in g[u]:

        if visited_edge[u][v] is False:

            visited_edge[u][v], visited_edge[v][u] = True, True

            path = dfs(v, g, visited_edge, path)

    return path

def isconnected():

    visited_edge = [[False for _ in range(n + 1)] for _ in range(n + 1)]

    v = random.choice(list(g))

    path = dfs(1, g, visited_edge)

    return path

def degrees():

    for v, list in g.items():
        d[v] = len(list)
    
    for v in g.keys():
        for u, list in g.items():
            if v in list and v != u:
                d[v] = d[v] + 1
    
    for v, list in d.items():
        if list % 2 != 0:
            return False

    return True

def iseulerian():
    return isconnected() and degrees()

def remocaoArestas(vertice, aresta):
  
  if vertice in g.keys():                                                                    
    if aresta in g[vertice]:                                                                 
        g[vertice].remove(aresta)
        g[aresta].remove(vertice)                                                           

def number_edges(graph):
    aux = 0
    for v, list in graph.items():
        aux = aux + len(list)
    return aux

def deque_to_tour(deque):
    path = []

    while deque:
        path.append(deque.pop())
        
    path.append(path[0])
    return path

def hierholzer():
    if iseulerian():
        path = deque()
        h = g.copy()
        current_vertex = random.choice(list(h))
        while number_edges(h) > 0:
            if d[current_vertex] > 0:
                next_vertex = random.choice(list(h[current_vertex]))
                path.append(next_vertex)
                remocaoArestas(current_vertex, next_vertex)
                # Tem que tirar as arestas do para diminuir o grau!
                current_vertex = next_vertex
            else:
                current_vertex = path.pop()
                path.append(next_vertex)
        return deque_to_tour(path)

if __name__ == '__main__':
    print(hierholzer())
