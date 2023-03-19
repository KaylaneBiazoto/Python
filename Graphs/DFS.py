grafo = {
    '0': ['1', '3'],
    '1': ['0', '4'],
    '2': ['6'],
    '3': ['0'],
    '4': ['3', '5', '7'],
    '5': ['4', '2'],
    '6': ['5'],
    '7': ['3'],
    '8': ['9'],
    '9': []
}

cor = {}
pred = {}
d = {}

tempo = 0
f = {}
aresta = {
    'arvore' : [],
    'retorno' : [],
    'cruzamento' : [],
    'avanco' : []
}

def DFS():

    for ver in grafo.keys():
        cor[ver] = 'branco'
        pred[ver] = None

    for ver in grafo.keys():
        if cor[ver] == 'branco':
            dfsVisit(ver)

def dfsVisit(u):

    global tempo
    tempo = tempo + 1
    cor[u] = 'cinza'
    d[u] = tempo

    for v in grafo[u]:
        if cor[v] == 'branco':
            pred[v] = u
            aresta['arvore'].append((u,v))
            dfsVisit(v)
        elif cor[v] == 'cinza':
            aresta['retorno'].append((u,v))
        elif cor[v] == 'preto':
            if d[u] < d[v]:
               aresta['avanco'].append((u,v))
            elif d[u] > d[v]:
               aresta['cruzamento'].append((u,v))
            
    cor[u] = 'preto'
    tempo += tempo
    f[u] = tempo

DFS()
print (aresta)
