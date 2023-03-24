# . . . . . . . . . . . . Leitura do arquivo . . . . . . . . . . . . #

txt = input('Nome do arquivo: ')                     #1 

with open(txt, 'r') as arq:                          #1
    grafo = {}                                       #1
    lista = []                                       #1

    tipo_grafo = arq.readline()                      #1
    tipo_grafo = tipo_grafo.strip('\n')              #1

    for linha in arq:                                #n
      lista.append(list(linha.strip()))              #m  
    
    for i in range(len(lista)):                      #n
      if lista[i][0] not in grafo.keys():            #n
        grafo[lista[i][0]] = []                      #1                                                                 
        grafo[lista[i][0]].append(lista[i][2])       #1
      else:                                          #1
        grafo[lista[i][0]].append(lista[i][2])       #1
    
    for aresta in grafo.copy().values():             #n²
      for i in range(len(aresta)):                   #n
          if aresta[i] not in grafo.keys():          #n
              grafo[aresta[i]] = []                  #1

                                #     => Complexidade total: O(n⁵)

# . . . . . . . . . . . . Inserção de Vértices . . . . . . . . . . . . #

def insercaoVertices(vertice): 
  print(f'\n 1). Inserção do vértice "{vertice}" no Grafo "{tipo_grafo}":')   #1
  print(f'\n\t Antes da inserção: \n\t{grafo}')                               #n   

  if vertice not in grafo.keys():                                             #n
    grafo[vertice] = []                                                       #1
  else:
    print(f'\n O vértice "{vertice}" já existe.\n')                           #1
    return                                                                    #1
  
  print(f'\n\t Depois da inserção: \n\t{grafo}')                              #n   

                                #     => Complexidade total: O(n) 

# . . . . . . . . . . . . Inserção de Arestas . . . . . . . . . . . . #

def insercaoArestas(vertice, aresta): 
  print(f'\n 2). Inserção da aresta "{aresta}" no vertice "{vertice}" do Grafo "{tipo_grafo}":') #1
  print(f'\n\t Antes da inserção: \n\t{grafo}')                                                  #n   

  if vertice in grafo.keys():                                                                    #n
    if aresta not in grafo[vertice]:                                                             #n 
      if tipo_grafo == 'directed':                                                               #1
        grafo[vertice].append(aresta)                                                            #1
      else:                                                                                      #1
        grafo[vertice].append(aresta)                                                            #1
        grafo[aresta].append(vertice)                                                            #1
    else:                                                                                        #1
        print(f'\n\t A aresta "{aresta}" já está contida no vértice "{vertice}".')               #1
        return                                                                                   #1
  else:                                                                                          #1
    print('\n\t O vértice ou aresta não existe.')                                                #1
    return                                                                                       #1

  print(f'\n\t Depois da inserção: \n\t{grafo}')                                                 #n 

                                #     => Complexidade total: O(n²)

# . . . . . . . . . . . . Remoção de Vértices . . . . . . . . . . . . #

def remocaoVertices(vertice): 
  print(f'\n 3). Remoção do vértice "{vertice}" do Grafo "{tipo_grafo}":')  #1  

  print(f'\n\t Antes da remoção: \n\t{grafo}')                              #n   

  if vertice in grafo.keys():                                               #n
    del grafo[vertice]                                                      #n
    for vertices, arestas in grafo.items():                                 #n
        if vertice in arestas:                                              #n 
            grafo[vertices].remove(vertice)                                 #n
  else:                                                                     #1
    print(f'\n\t O vértice "{vertice}" não existe no grafo informado.')     #1
    return                                                                  #1
                                              
  print(f'\n\t Depois da remoção: \n\t{grafo}')                             #n

                                #     => Complexidade total: O(n⁵)

# . . . . . . . . . . . . Remoção das Arestas . . . . . . . . . . . . #

def remocaoArestas(vertice, aresta):  
  print(f'\n 4). Remoção da aresta "{aresta}" do vértice "{vertice}" do Grafo "{tipo_grafo}":')  #1  
  print(f'\n\t Antes da remoção: \n\t{grafo}')                                                   #n  

  if vertice in grafo.keys():                                                                    #n
    if aresta in grafo[vertice]:                                                                 #n
        grafo[vertice].remove(aresta)                                                            #n
    else:
        print(f'\n\t A aresta "{aresta}" não está contida no vértice "{vertice}".')              #1 
        return                                                                                   #1
  else:                                                                                          #1
    print(f'\n\t O vértice "{vertice}" não existe no grafo informado.')                          #1
    return                                                                                       #1

  print(f'\n\t Depois da remoção: \n\t{grafo}')                                                  #1

                                #     => Complexidade total: O(n³)

# . . . . . . . . . Mostra o grafo . . . . . . . . . #

def mostrarGrafos():
  print(f'\n 5). Grafo "{tipo_grafo}":\n\n\t{grafo}')      #n

                                #     => Complexidade total: O(n)

# . . . . . . . . . . . . . Matriz Adjacente . . . . . . . . . . . . . . #

def matrizAdjacente():
  print('\n 6). Matriz Adjacente do grafo:\n')                         #1

  qntdVertices = 0;                                                    #1
  
  for chave in grafo.keys():                                           #n
    qntdVertices += 1;                                                 #1

  matriz = [[0]*qntdVertices for i in range(qntdVertices)]             #n  

  for vertice_vertical, valor in enumerate(grafo):                     #n
    for vertice_horizontal, letra in enumerate(grafo):                 #n
      if letra in grafo[valor]:                                        #n
        matriz[vertice_vertical][vertice_horizontal] = 1               #1

  print(f'\t{matriz}')                                                 #n

                                #     => Complexidade total: O(n³)

# . . . . . . . . . . . . . Verifica as Arestas . . . . . . . . . . . . . #

def verificaAresta(vertice, aresta):
  print(f'\n 7). Verificando se a aresta "{aresta}" está contida no vértice "{vertice}"...')         #1
  if aresta in grafo[vertice]:                                                                       #n
    print(f'\n\t A aresta "{aresta}", do Grafo "{tipo_grafo}", existe no vértice "{vertice}".')      #1
  else :                                                                                             #1
    print(f'\n\t A aresta "{aresta}", do Grafo "{tipo_grafo}", NÃO existe no vértice "{vertice}".')  #1    
                                #     => Complexidade total: O(n)

# . . . . . . . . . . . . Vértices Adjacentes . . . . . . . . . . . . . #

def verticesAdjacentes(vertice):
    print(f'\n 8). Verificando os vértices adjacentes ao vértice "{vertice}"...')        #1
    if vertice not in grafo.keys():                                                      #n
      print(f'\n\t O vértice "{vertice}" não existe no grafo.')                          #1
      return                                                                             #1
    if tipo_grafo == 'directed':                                                         #1                                                         #1
      print(f'\n\t O vértice "{vertice}" é adjacente aos vértices "{grafo[vertice]}".')  #n
    elif tipo_grafo == 'undirected':                                                     #1
      list = grafo[vertice].copy()                                                              #1
      for vertices, arestas in grafo.items():                                            #n
        if vertice in grafo[vertices]:                                                   #n
            list.append(vertices)                                                       #1
      print(f'\n\t O vértice "{vertice}" é adjacente aos vértices "{list}".')           #n

                                #     => Complexidade total: O(n²)

# . . . . . . . . . . . Vértices Incidentes . . . . . . . . . . . . . #

def verticesIncidentes(vertice):
  print(f'\n 9). Verificando os vértices Incidentes ao vértice "{vertice}"...')         #1

  if vertice not in grafo.keys():                                                       #n
    print(f'\n O vértice "{vertice}" não existe no grafo.')                             #1
    return                                                                              #1
  if tipo_grafo == 'undirected':                                                        #1
    list = grafo[vertice].copy()                                                              #1 
  else:                                                                                 #1
    list = []                                                                          #1
    
  for chave, valor in grafo.items():                                                    #n
    if vertice in valor:                                                                #n
      list.append(chave)                                                               #1
  
  print(f'\n\t Os vértices incidentes em "{vertice}" são: "{list}".')                  #n

                                #     => Complexidade total: O(n²)

# . . . . . . . . . . . . Grafo Complemento . . . . . . . . . . . . . #

def grafoComplemento():   
  print('\n 10). Grafo Complemento:')                                     #1

  listaVerticesExistentes = []                                            #1
  listaArestasNaoExistentes = []                                          #1
  grafoComplementar = {}                                                  #1

  for chave in grafo.keys():                                              #n
    listaVerticesExistentes.append(chave)                                 #1
  for chave, valor in grafo.items():                                      #n
    for i in range(len(listaVerticesExistentes)):                         #n
      if listaVerticesExistentes[i] not in valor and listaVerticesExistentes[i] != chave:                         #n
        listaArestasNaoExistentes.append(listaVerticesExistentes[i])      #1
    grafoComplementar[chave] = listaArestasNaoExistentes                  #1
    listaArestasNaoExistentes = []                                        #1

  print(f'\n\t{grafoComplementar}')                                       #n

                                #     => Complexidade total: O(n³)

# . . . . . . . . . . . . Grafo Transposto . . . . . . . . . . . . . #

def grafoTransposto():
  print('\n 11). Grafo Transposto:')                              #1
  grafoTransposto = {}                                            #1

  for chave in grafo.keys():                                      #n
    grafoTransposto[chave] = []                                   #1

  for chave, valor in grafo.items():                              #n
    if valor != []:                                               #1
      for i in range(len(valor)):                                 #n
        grafoTransposto[valor[i]].append(chave)                   #1

  print(f'\n\t{grafoTransposto}')                                 #n

                                #     => Complexidade total: O(n²)

# . . . . . . . . . . . . Testes . . . . . . . . . . . . #


insercaoVertices('f')
insercaoArestas('f', 'a')
remocaoVertices('f')
remocaoArestas('b', 'a')
mostrarGrafos()
matrizAdjacente()
verificaAresta('b', 'e')
verticesAdjacentes('c')
verticesIncidentes('b')
grafoComplemento()
grafoTransposto() 


# a { d }
# b { a }
# c { a b d }
# d { a b c }

# a b => a {}
# a c => b { a }
# b c => c { a b }
# b d => d { b }

# 10). Grafo Complemento:

#         {'a': ['a', 'd'], 'b': ['a', 'b'], 'c': ['a', 'b', 'c', 'd'], 'd': ['a', 'b', 'c', 'd']}

#  11). Grafo Transposto:

#         {'a': [], 'b': ['a'], 'c': ['a', 'b'], 'd': ['b']}
