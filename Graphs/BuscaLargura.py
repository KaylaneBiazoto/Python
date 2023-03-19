txt = input('Nome do arquivo: ')                     

with open(txt, 'r') as arq:                          
    grafo = {}                                       
    lista = []                                       

    tipo_grafo = arq.readline()                      
    tipo_grafo = tipo_grafo.strip('\n')              

    for linha in arq:                                
      lista.append(list(linha.strip()))               
    
    for i in range(len(lista)):                      
      if lista[i][0] not in grafo.keys():            
        grafo[lista[i][0]] = []                                                                                      
        grafo[lista[i][0]].append(lista[i][2])       
      else:                                          
        grafo[lista[i][0]].append(lista[i][2])       
    
    for aresta in grafo.copy().values():             
      for i in range(len(aresta)):                   
          if aresta[i] not in grafo.keys():          
              grafo[aresta[i]] = []                  


cor = {}
d = {}
pred = {}

def inicializa(u):

    for v in grafo.keys():
        cor[v] = 'branco'
        d[v] = -1
        pred[v] = None
    
    cor[u] = 'cinza'
    d[u] = 0
    pred[u] = None

def insere(q, v):
    q.append(v)

def remove(q):
    q.pop(0)

def buscaEmLargura(u):
    queue = []
    inicializa(u)
    insere(queue, u)
    
    while len(queue) > 0:

        remove(queue)

        for adj in grafo[u]:
            if cor[adj] == 'branco':
                cor[adj] = 'cinza'
                d[adj] = d[u] + 1
                pred[adj] = u
                insere(queue, adj)

        cor[u] = 'preto'
        if queue != []:
            u = queue[0]

def imprimeCaminho (origem, destino):
    if origem == destino:
        print(origem)
    else:
        if pred[destino] == None:
            print(f'Não existe caminho de {origem} até {destino}')
        else:
            imprimeCaminho(origem, pred[destino])
            print(destino)

buscaEmLargura('1')
imprimeCaminho('1','3')
