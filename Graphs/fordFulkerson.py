# Aumenta(G,P, f)
# 1 Seja b o Gargalo(P, f)
# 2 for cada aresta (u, v) ∈ P do
# 3 if (u, v) é uma aresta de avanço then
# 4 Incremente f(u, v) em G em b unidades
# 5 else
# 6 Decremente f(u, v) em G em b unidades;


# Ford-Fulkerson(G)
# 1 Inicialmente f(u, v) = 0 para toda aresta (u, v) ∈ G.E
# 2 while existir caminho aumentante no grafo residual Gf do
# 3 Seja P um caminho simples de s a t em Gf
# 4 Aumenta(G,P, f)

from math import inf
g = {
    's': [(40, 'a'), (40, 'b')],
    'a': [(10, 'd'), (10, 'd')],
    'b': [(10, 'c'), (20, 'e')],
    'c': [(20, 'd'), (10, 'e'),(10, 't')],
    'd': [(30, 't')],
    'e': [(20, 't')],
    't': []
}

def BFS(s, t, pred):

    visited = {}
    queue = []
    queue.append(s)

    for v in g:
        visited[v] = False
    visited[s] = True
    pred[s] = None

    while queue:
        u = queue.pop(0)
        for ind in g[u]:
            if visited[ind[1]] is False:
                queue.append(ind[1])
                visited[ind[1]] = True
                pred[ind[1]] = u

    return True if visited[t] else False

def fordFulkerson(source, sink):
    f = {}
    for v, u in g.items():
        for i in range(len(u)):
            f[(v,u[i][1])] = 0
    
    pred = {}
    while BFS(source, sink, pred):

        flow = inf
        t = sink
        flow_max = 0

        while t != source:
            for u, v in g[pred[t]]:
                if v == t:
                    flow = min(flow, u)
                    t = pred[t]
    
        flow_max = flow_max + flow
        v = sink

        while v != source:
            u = pred[v] 
            for b, a in g[u]:
                if v == a:
                    c = b - flow
                    g[u].remove((b, a))
                    g[u].append((c,a)) 
            v = pred[v]

        print(g)
        print(flow_max)

    return flow_max
            
                
print(fordFulkerson('s', 't'))

https://python.algorithmexamples.com/web/networking_flow/ford_fulkerson.html
https://www2.hawaii.edu/~nodari/teaching/s18/Notes/Topic-20.html
    