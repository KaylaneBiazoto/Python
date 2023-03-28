# Kethelyn Corrêa Andrade RA: 124791, Kaylane Biazoto         RA: 124078

import random
from heapq import heappop, heappush, heapify
from math import inf

# . . . . . Leitura do arquivo . . . . . #

txt = 'graph.txt'                      

with open(txt, 'r') as arq:  

    g = {}                                    
    lista = []                                       

    tipo_grafo = arq.readline()                      
    tipo_grafo = tipo_grafo.strip('\n')              

    for linha in arq:                                
      lista.append(list(linha.strip()))                
    
    for i in range(len(lista)):   
                         
      if lista[i][0] not in g.keys():            
        g[lista[i][0]] = []     # Se não existe cria uma key no graph pq senão o append não funciona                                                                                      
      g[lista[i][0]].append((int(lista[i][4]), lista[i][2])) # se ja existe não precisa criar a lista vazia, só faz o append direto || # i0 é a primeira letra, i4 é o numero e i2 é a segunda letra. Usa o int pra transformar em numero os char

      if tipo_grafo == 'undirected': # se for undirected tem que colocar a outra letra recebendo o vertice tbm pq é via dupla
        if lista[i][2] not in g.keys(): # primeiro ve se não é uma chave pq se não tem que adicionar ela como uma lista vazia
           g[lista[i][2]] = []
        g[lista[i][2]].append((int(lista[i][4]), lista[i][0])) 

    n = len(g) # pega a qtnd de vertice do grafo      

# . . . . . Prim (Guloso e Árvore Geradora Mínima) . . . . . #

def dfs(u, path = [], visited = set()):

    path.append(u) # bota  o vertice
    visited.add(u) # bota q ja foi visitado

    if u in g: # ve se o vertice é uma chave do g senão dá ruim
        for adj in g[u]: # se for, pega os ajacentes dele e faz a visita
            if adj[1] not in visited: # verifica se ele já foi visitado né
                dfs(adj[1]) # vai visitar geral recursivamente. Se tiver um vertice que não tem aresta conectando a ele, n vai ter um caminho

    return path

def isconnected():

    v = random.choice(list(g)) # Pega um vertice aleatorio pra começar a busca

    path = dfs(v) # chama o dfs

    return path

def MST_Prim(s):
   
   if isconnected() and tipo_grafo == 'undirected': # pra poder fazer o prim precisa ser conectado e undirected. Aí pra ver se é conectado faz ou BFS ou DFS
      
    chave = {}
    pai = {}

    for u in g.keys():
        chave[u] = inf
        pai[u] = None

    chave[s] = 0
    Q = [(0, s)] # A gente vai colocar um por um ao invés de todos os v de uma vez pq é menos caro eu acho

    while Q:
       w, u = heappop(Q)  # extract_min. Pega 0 e s inicialmente
       for dist, v in g[u]: # vai pegar um por um a w dos adj de u, assim como os v
          if v not in Q and w < chave[v]: # vai ver se 0 de v é menor que a chave[v] que é inf
                pai[v] = u  # o predecessor de v é u pq vai formar uma "arvore" MST no final
                chave[v] = w # a nova chave de v vai ser a soma pq é obviamente menor que infinito
                heappush(Q, (w, v)) # bota os novos valores em Q
    
    print (chave)
    print (pai)

# . . . . . Dijkstra (Caminho Mínimo) . . . . . #

def initialize_single_source(s):

    d = {}
    pred = {}                               

    for v in g:                        
        d[v] = inf
        pred[v] = None
    
    d[s] = 0

    return d, pred

def relax(w, u, Q, d, p):

    for dist, v in g[u]:
        if (w + dist) < d[v] and v not in Q:
            d[v] = w + dist
            p[v] = u
            heappush(Q, ((w + dist), v))

def dijkstra(s):
   
   d, p = initialize_single_source(s)
   Q = [(0, s)]
   
   while Q:
      w, u = heappop(Q)      # extract_min
      relax(w, u, Q, d, p)

   print (d)
   print(p)

# . . . . . Kruskal (Árvore Geradora Mínima) . . . . . #  

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

def link(x, y):

    if rank[x] > rank[y]: 
        parent[y] = x
    else:
        parent[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1

def union(x, y):
    link(find_set(x), find_set(y))

def MST_Kruskal():
    
    A = []

    for v in g.keys():
        make_set(v)

    # Ordenando em ordem crescente de peso
    Q = get_edges()
    #heapify(Q)
    Q = sorted(Q)

    for peso, pred, suce in Q:
        if find_set(pred) != find_set(suce):
            A.append((peso,pred,suce))
            union(pred, suce)
            #heappop(Q)
            
    print("Minimal Spanning Tree:")
    for weight, u, v in A:
            print("%c - %c: %d" % (u, v, weight))

# . . . . . Bellman-Ford (Caminho Mínimo) . . . . . # 

if __name__ == "__main__":

    choices = [v for v in g]
    choice = ""
    
    while choice not in choices:
        print("Pick a starting point from the following list:")
        for _choice in choices:
            print(" - " + _choice)
        choice = input("> ")

    # MST_Prim(choice) # Não funciona em grafos direcionados, devolve a MST, pode trabalhar com aresta negativa
    # dijkstra(choice) # Funciona para undirected e directed, devolve o menor caminho NÃO A MST, não pode ter aresta negativa!
    
    # Dijkstra’s algorithm is used when we want to save time and fuel traveling from one point to another. 
    # Prim’s algorithm is used when we want to minimize material costs in constructing roads that connect multiple points to each other.
    # No algoritmo, a diferença está no relax, que o Prim n tem o + dist e o Dijkstra tem

    # MST_Kruskal() # Também devolve uma árvore geradora mínima, usa o corte e pode trabalhar com ciclos
    # O Heapq não tá funcionando nele, dar uma olhada nisso depois!