# Ver se tem ciclo: https://marcodiiga.github.io/minimum-spanning-tree

from math import inf
from heapq import heapify, heappush, heappop

g = {
        'a': [(60, 'b'), (10, 'c'), (40, 'd')],
        'b': [(60, 'a'), (20, 'd'), (30, 'c')],
        'c': [(10, 'a'), (50, 'd'), (30, 'b')],
        'd': [(50, 'c'), (20, 'b'), (40, 'a')]
    }

parent = {}
rank = {}

def make_set(x):
    
    parent[x] = x
    rank[x] = 0

def get_edges():

    edges = []

    for (x, y) in g.items():

        for i, j in y:
            temp = (i, x, j)
            edges.append(temp)
    
    return edges

def find_set(x):

    if parent[x] != x:
        parent[x] = find_set(parent[x])

    return parent[x]

def union(x, y):
    link(find_set(x), find_set(y))

def link(x, y):

    if rank[x] > rank[y]: 
        parent[y] = x
    else:
        parent[x] = y
        if rank[x] == rank[y]:
            rank[y] = rank[y] + 1

def kruskal():

    A = []

    for v in g.keys():
        make_set(v)

    # Ordenando em ordem crescente de peso
    Q = get_edges()
    heapify(Q)

    for peso, pred, suce in Q:
        if find_set(pred) != find_set(suce):
            A.append((suce))
            union(pred, suce)
            
    print(A)
    
kruskal()

# https://gist.github.com/thbighead/5aac5a34352ed6655276c43900560f84