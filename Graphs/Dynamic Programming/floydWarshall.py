from math import inf

graph = [
    [0, 3, 8, inf, -4],
    [inf, 0, inf, 1, 7],
    [inf, 4, 0, inf, inf],
    [2, inf, -5, 0, inf],
    [inf, inf, inf, 6, 0]
]

n = len(graph)  

def floydWarshall(graph,n):
    dist = graph
    p = [[None] * n for i in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0 and graph[i][j] != inf:
                p[i][j] = i + 1
            else:
                p[i][j] = None
    

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if (dist[i][k] + dist[k][j] < dist[i][j]):
                    dist[i][j] = dist[i][k]+dist[k][j]
                    p[i][j] = p[k][j]
    
                #dist[i][j] = min(dist[i][j], dist[i][k]+ dist[k][j])
          
    print(dist)
    print(p)
    return dist

floydWarshall(graph, n)

# https://github.com/Herculest619/Problema-do-caminho-minimo-Dijkstra-Bellman-Ford-Floyd-Warshall
