import random
from heapq import heappop, heappush, heapify
from math  import inf

# . . . . . Leitura do arquivo . . . . . #

g = {}

def addInGraph(i, n1, n2, lista):

 if lista[i][4] == '-':
     if len(lista[i]) > 6:
       aux = lista[i][4] + lista[i][5] + lista[i][6]
       g[lista[i][n1]].append(((int(aux)), lista[i][n2]))
     if len(lista[i]) <= 6:
       aux = lista[i][4] + lista[i][5]
       g[lista[i][n1]].append(((int(aux)), lista[i][n2]))

 if lista[i][4] != '-' and len(lista[i]) == 6:
     aux = lista[i][4] + lista[i][5]
     g[lista[i][n1]].append(((int(aux)), lista[i][n2]))
 elif lista[i][4] != '-':
     g[lista[i][n1]].append(((int(lista[i][4])), lista[i][n2]))

def leitura_grafo():

 txt = 'graph.txt'              

 with open(txt, 'r') as arq:
                         
   lista = []                            

   tipo_grafo = arq.readline()              
   tipo_grafo = tipo_grafo.strip('\n')      

   for linha in arq:                        
     lista.append(list(linha.strip()))

   for i in range(len(lista)):
     if lista[i][0] not in g.keys():
         g[lista[i][0]] = []
         addInGraph(i, 0, 2, lista)
     elif lista[i][0] in g.keys():
         addInGraph(i, 0, 2, lista)
 return tipo_grafo, lista

def existencia_vertice(lista):
  for i in range(len(lista)):
    if lista[i][2] not in g.keys():
       g[lista[i][2]] = []
     
def leitura_undirected(lista,):
   for i in range(len(lista)):
     if lista[i][2] not in g.keys():
       g[lista[i][2]] = []
       addInGraph(i, 2, 0, lista)
     elif lista[i][2] in g.keys():
       addInGraph(i, 2, 0, lista)

def leitura_arquivo():

  lista = []

  tipo_grafo, lista = leitura_grafo()

  if tipo_grafo == 'undirected':
      leitura_undirected(lista)
  elif tipo_grafo == 'directed':
     existencia_vertice(lista)

  return tipo_grafo

def initialize_single_source(s, d, pred):
                     
 for v in g:                  
   d[v] = inf
   if type(pred) == dict:
     pred[v] = None
   elif type(pred) == list:
     pred.append(v)

 d[s] = 0

def get_edges():

   edges = []

   for (x, y) in g.items():
     for i, j in y:
         temp = (i, x, j)
         edges.append(temp)
 
   return edges

# . . . . . Prim . . . . . #

def dfs(u, path = [], visited = set()):

 path.append(u)
 visited.add(u)


 if u in g:
   for adj in g[u]:
     if adj[1] not in visited:
       dfs(adj[1])

 return path

def isconnected():

 v = random.choice(list(g))

 path = dfs(v)

 return path

def MST_Prim(s, tipo_grafo):

 print ('\033[0;49;34m'+ "\n\t * Algoritmo de Prim *" + '\033[0;0m')

 if isconnected() and tipo_grafo == 'undirected':
   chave = {}
   pai = {}
   added = set()
 else:
    return (print("\n O grafo é 'directed'! Não é possível gerar a Árvore Geradora Mínima."))

 initialize_single_source(s, chave, pai)

 chave[s] = 0
 Q = []
 heappush(Q, (0,s))

 while Q:
   w, u = heappop(Q)
   if u in added:
     continue
   added.add(u)
   for dist, v in g[u]:
     if v not in added and dist < chave[v]:
       pai[v] = u
       chave[v] = dist
       heappush(Q, (dist, v))

 print (f"\n Custo: {chave}")
 print (f"\n Árvore Geradora Mínima: {pai}\n")

# . . . . . Kruskal . . . . . #

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

 print('\033[0;49;34m' + '\n\t * Algoritmo de Kruskal *' + '\033[0;0m')

 if isconnected():
   A = []
 else:
   return
 
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
 
 print("\n Árvore Geradora Mínima:")
 for peso, u, v in A:
   print("\n\t%c - %c: %d" % (u, v, peso))

# . . . . . Dijkstra  . . . . . #

def is_negative():

 for (x, y) in g.items():
     for i, j in y:
         if i < 0:
            return True
       
 return False

def relax(w, u, Q, d, p):

   for dist, v in g[u]:
     if (w + dist) < d[v] and v not in Q:
       d[v] = w + dist
       p[v] = u
       heappush(Q, ((w + dist), v))

def dijkstra(s):
   
   print ('\033[0;49;34m' + "\n\n\t * Algoritmo de Dijkstra *" + '\033[0;0m')

   if is_negative():
      return (print("\n O grafo possuí arestas negativas! Não é possível gerar o Caminho Mínimo pelo Dijkstra."))

   d = {}
   p = {}

   initialize_single_source(s, d, p)
   Q = [(0, s)]
 
   while Q:
     w, u = heappop(Q)   # extract_min
     relax(w, u, Q, d, p)

   print (f"\n Custo: {d}")
   print (f"\n Caminho Mínimo: {p}\n")

# . . . . . Bellman-Ford . . . . . #

def return_Edges():
 
   edges = {}

   for v, tuple in g.items():
     for w, u in tuple:
       edges[(v, u)] = w  # u --w--> v

   return edges

def bellman_ford(n_vertice, s):
 
   ''' True = sem ciclo negativo '''
   print ('\033[0;49;34m' + "\n\t * Algoritmo de Bellman Ford *" + '\033[0;0m')

   edges = {}
   edges = return_Edges()

   dist = {}
   pred = {}

   initialize_single_source(s, dist, pred)              

   # relax
   for round in range(1, n_vertice + 1):
     for edge, w in edges.items():
       u, v = edge
       if dist[v] > (dist[u] + w):
         if round != n_vertice:
           dist[v] = dist[u] + w
           pred[v] = u
         else:
           print ("\n     Ciclo negativo:")
           print (f"\n Custo: {dist}")
           print (f"\n Caminho Mínimo: {pred}")
           return False, dist # Possuí ciclo negativo
 
   print (f"\n Custo: {dist}")
   print (f"\n Caminho Mínimo: {pred}")
 
   return True, dist

# . . . . . Floyd Warshall (Caminho Mínimo) . . . . . #

def matriz(matriz):
                     
 for vertice_vertical, valor in enumerate(g):                    
   for vertice_horizontal, letra in enumerate(g):
     for i in range(len(g[valor])):              
       if letra in g[valor][i]:                                      
           matriz[vertice_vertical][vertice_horizontal] = g[valor][i][0]
       if vertice_horizontal == vertice_vertical:
          matriz[vertice_vertical][vertice_horizontal] = 0                                                  

def print_path(p, v, u, route):
 
  if p[v][u] == v:
       return
  print_path(p, v, p[v][u], route)
  route.append(p[v][u])
 
def print_solution (p, v, u):
  if u != v and p[v][u] != None:
   route = [v]
   print_path(p, v, u, route)
   route.append(u)
   print(f'\n Caminho Mínimo de {v} até {u}: ', route)
     
def floyd_Warshall(n, choice):
   
   print('\033[0;49;34m' + "\n\n\t * Algoritmo de Floyd Warshall *" + '\033[0;0m')

   print("\n\t\t - - -")
   ciclo_negativo, b = bellman_ford(n, choice)
   print("\n\t\t - - - \n")
 
   graph = [[inf] * n for i in range(n)]
   matriz(graph)

   dist = graph
   p = [[None for x in range(n)] for y in range(n)]

   for i in range(n):
     for j in range(n):
       if i == j:
          p[i][j] = 0
       elif dist[i][j] != inf:
          p[i][j] = i
       else:
          p[i][j] = -1

   for k in range(n):
       for i in range(n):
           for j in range(n):
               if (dist[i][k] + dist[k][j] < dist[i][j]):
                   dist[i][j] = dist[i][k] + dist[k][j]
                   p[i][j] = p[k][j]
 
   print(f"\n Custo: {dist}")
   print(f"\n\n Predecessores: {p}")

   if ciclo_negativo == True:
     print_solution(p, 0, 2)
   else:
      print("\n O grafo possuí um ciclo negativo. Não é possível gerar o Caminho Mínimo.")

# . . . . . Main . . . . . #

if __name__ == "__main__":
    
    tipo_grafo = leitura_arquivo()

    print('\033[0;49;34m' + '\n\t Grafo:\n\n' + '\033[0;0m' + f'{g}\n\n')

    n = len(g)
    choices = [v for v in g]
    choice = ""

    while choice not in choices:
        print("Escolha um vértice para começar:")
        for _choice in choices:
            print(" - " + _choice)
        choice = input("> ")

    MST_Prim(choice, tipo_grafo) # undirected
    input()
    MST_Kruskal() # conexo
    input()
    dijkstra(choice) # apenas com positivos
    input()
    bellman_ford(n, choice) # permite negativo
    input()
    floyd_Warshall(n, choice) # permite negativo
