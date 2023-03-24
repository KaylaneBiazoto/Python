from math import inf
from heapq import heapify, heappush, heappop

g = {
    's': [(-1, 't'), (4, 'y')],
    't': [(3, 'y'), (2, 'z'), (2,'x')],
    'x': [(-3, 'z')],
    'y': [],
    'z': [(5, 'y'), (1, 't')]
}

def bellman_ford(n_vertice: int, source = chr) -> bool:
    ''' returns True (no negative cycle) / False (cycle) and distance array '''
    
    # data import
    edges = {}
    for v, tuple in g.items():
        for w, u in tuple:
            edges[(v, u)] = w  # u --w--> v

    # set initial distance and predecessors
    distance = {}
    pred = []                       

    for v in g:
        if v == source:
            distance[v] = 0 
        else:                       
            distance[v] = inf
            pred.append(None)

    # relax
    for round in range(1, n_vertice + 1):  # for n rounds ...
        for edge, w in edges.items():  # relax all edges
            u, v = edge
            if distance[v] > distance[u] + w:
                if round != n_vertice:
                    distance[v] = distance[u] + w
                    pred.append(u)
                else:  # n-th round for cycle detection
                    return False, distance
    
    return True, distance

print(bellman_ford(5, 's'))
