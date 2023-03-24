from heapq import heappop, heappush
from math import inf

g = {
        'A': [(4, 'B'), (2, 'C')],
        'B': [(4, 'A'), (1, 'C'), (5, 'D')],
        'C': [(2, 'A'), (1, 'B'), (8, 'D'), (10, 'E')],
        'D': [(5, 'B'), (8, 'C'), (2, 'E')],
        'E': [(10, 'C'), (2, 'D')]
    }

def MST_Prim(s):

    chave = {}
    pai = {}

    for u in g.keys():
        chave[u] = inf
        pai[u] = None

    chave[s] = 0

    Q = [(0, s)]

    while Q:

        total, u = heappop(Q)      # extract_min
        for dist, v in g[u]:
            new_total = total + dist
            if v not in Q and new_total < chave[v]:
                pai[v] = u
                chave[v] = new_total
                heappush(Q, (new_total, v))

    print(chave)
    print(pai)

MST_Prim('A')