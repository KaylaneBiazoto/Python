# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
#      Alunas: Kaylane Biazoto             R.A.: 124078       .
#              Kethelyn Corrêa Andrade     R.A.: 124791       . 
# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 

import numpy as numpy
import sys
import re

def formatacaoDaMatriz(matriz):
    fomata_linha = ['\n\t' + ''.join(['{:4}'.format(item) for item in linha]) if i > 0 else ''.join(['{:4}'.format(item) for item in linha]) for i, linha in enumerate(matriz)]
    return '\n\t' + '\n\t'.join(fomata_linha)

def terminateProgram():
    import sys
    print("\n\n\t\t_________________________")
    print("\t\t_________________________")
    print("\n\t\tError")
    print("\t\tTerminating Program")
    print("\t\t_________________________")
    print("\t\t_________________________\n\n\n")
    sys.exit()


def main():
    iteracoes =0

    print("Seja bem-vindo(a) ao Método Simplex! 🤓")

    metodo = Metodo_do_simplex() # Cria um objeto

    matriz_funcaoObjetiva = (metodo.primeiraEquivalencia()).reshape(1, -1) # Chama a primeira equivalência que é max ou min
    
    # O primeiro argumento de reshape é 1, o que significa que você deseja que a matriz resultante tenha 1 linha.
    # O segundo argumento é -1, que é usado para dizer ao NumPy para determinar automaticamente o número apropriado de colunas para que o número total de elementos seja o mesmo que na matriz original.
    # Portanto, o reshape está sendo usado para transformar a matriz retornada por metodo.primeiraEquivalencia() em uma matriz bidimensional com uma única linha.

    copia_matrizObjetiva = numpy.copy(matriz_funcaoObjetiva) # Isso vai ser usado para substituir os valores encontrados na função objetiva.

    qntd_restricoes, qntd_variaveisDecisao = metodo.informacoesDasRestricoes() # Pega qntd dos 2 para fazer a matriz
    
    matriz, base, nao_base, b, cbt, cnt, indices_variaveis = metodo.criarMatriz(qntd_restricoes, qntd_variaveisDecisao, matriz_funcaoObjetiva) # Vai criar as matrizes para fazer o problema

    for i in range (qntd_restricoes + 1): # como só pode ter iterações iguais a qntd de restrições. Mas tem um caso dos exercicio que foi pra +1 e nao terminou inteiro, ent existe esse +1 ai
        if i > (qntd_restricoes + 1): # se ultrapassar tá errado
            terminateProgram()
        else:
            input() 
            iteracoes += 1
            print(f"\n\t\t\t* Iteração {iteracoes} *\n")
            matriz, base, nao_base, b, cbt, cnt, indices_variaveis = metodo.iteracoes(matriz, base, nao_base, b, cbt, cnt, copia_matrizObjetiva, indices_variaveis) 

class Metodo_do_simplex:
    
    def primeiraEquivalencia(self): 
        
        problemaEscolhido = {
            1: "Problema de Maximização",
            2: "Problema de Minimização"
        }

        while True:
            print("\n\tInforme o tipo do problema:" 
                  + "\n\n\ta) Pressione 1 para um Problema de Maximização;" 
                  + "\n\tb) Pressione 2 para um Problema de Minimização;")

            try:
                tipoDoProblema = int(input("\n\tOpção escolhida: "))
                
                if tipoDoProblema in problemaEscolhido:
                    print("\n\n\t\t      . . . . . . . . . . . . . . .")
                    print("\t\t\t", problemaEscolhido[tipoDoProblema])
                    print("\t\t      . . . . . . . . . . . . . . .")

                    metodo = self.funcaoObjetiva(tipoDoProblema) # Vau escolher 1 ou 2 das opções. Aí cria uma função objetiva
                    
                    return metodo
                else:
                    print("\n\t\t\t🚨 Atenção 🚨"
                          + "\n\tOpção Inválida. Por favor, pressione 1 ou 2.\n\t\t\t  . . . . .")

            except ValueError:
                print("\n\t\t\t🚨 Atenção 🚨\n\tOpção Inválida."
                      + "Por favor, pressione 1 ou 2.\n\t\t\t  . . . . .")

    def informacoesDasRestricoes(self):
       
        print("\n\t• Qual o número total de Restrições?")
        qntd_restricoes = int(input("\n\t\t"))

        print("\n\t• Qual o número total de Variáveis de Decisão?")
        qntd_variaveisDecisao = int(input("\n\t\t"))

        return qntd_restricoes, qntd_variaveisDecisao
 
    def criarMatriz(self, qntd_variaveisDecisao, qntd_restricoes, matriz_funcaoObjetiva):
        
        matriz = numpy.zeros((qntd_variaveisDecisao, qntd_variaveisDecisao + qntd_restricoes)) # linha = qntd de decisao | coluna = qntd decisao + qntd restricao pq vai adicionar os 1 e os 0
        b = numpy.zeros((qntd_variaveisDecisao, 1)) # b vai ter 1 coluna e várinhas linhas

        base = numpy.zeros((qntd_variaveisDecisao, qntd_variaveisDecisao)) # como a base vai ser a identidade, é a quantidade de variaveis de decisao         
        nao_base = numpy.zeros((qntd_variaveisDecisao, qntd_restricoes)) 

        cbt = numpy.zeros ((1, qntd_variaveisDecisao)) # só tem 1 linha
        cnt = matriz_funcaoObjetiva # dá para copiar a matriz da funcao objetiva já que é igual.

        indices_variaveis = [] # vai começar a guardar os índices para usar no xb

        for linha_atual in range (qntd_variaveisDecisao): # Vai fazer isso pela quantidade de decisoes
            matriz, base, nao_base, b, cbt, indices_variaveis = self.processamentoDeUmaLinha(matriz, base, nao_base, b, cbt, linha_atual, qntd_restricoes, indices_variaveis)  # vai criar as inequacoes

        return matriz, base, nao_base, b, cbt, cnt, indices_variaveis

    def processamentoDeUmaLinha(self, matriz, base, nao_base, b, cbt, linha, qntd_restricoes, indices_variaveis):
        
        print("\n\tInforme os valores das restrições:")

        # Itera sobre as colunas (variáveis de restrição) para obter os valores e preencher a matriz
        for coluna in range (qntd_restricoes):
            valor = self.getValorDaMatriz(linha, coluna)   # recebe a linha lá de cima e a coluna itera aqui       
            matriz[linha, coluna] = valor # cria a coluna aq
            nao_base[linha, coluna] = valor # cria a nao base aqui, assumindo que a identidade vai ser a base

        operador = self.getOperadorCondicional()
        
        if operador == '<=':
            matriz[linha, qntd_restricoes + linha] = 1 # se for menor coloca a variavel de folga como 1
            base[linha, linha] = 1 #  a base vai recber a identidade
            indices_variaveis.append(qntd_restricoes + linha) # vai ser o indice xo xb
        elif operador == '>=':
            matriz[linha, qntd_restricoes + linha] = -1
            base[linha, linha] = -1
            indices_variaveis.append(qntd_restricoes + linha)  
        else:
            terminateProgram()

        valor_inequacao = self.getValorDaComparacao()          

        if valor_inequacao < 0: # se for -1 tem que multiplicar a equação tudo
            matriz[linha] = matriz[linha] * -1
            b[linha, 0] = valor_inequacao * -1
            cbt[0] = 0
        else:
            b[linha, 0] = valor_inequacao # coloca no b normal
            cbt[0] = 0

        return matriz, base, nao_base, b, cbt, indices_variaveis

    def getValorDaMatriz(self, linha, coluna):
        return float(input(f"\n\t\tLinha {linha+1} - Coluna {coluna+1}: "))

    def getOperadorCondicional(self):
        print("\n\t• Escolha o tipo de operador condicional. <=, => or =")
        return input("\n\t\t")

    def getValorDaComparacao(self):
        print("\n\t• Qual o valor da comparação?")
        return float(input("\n\t\t"))
    
    def funcaoObjetiva(self, tipoDoProblema):

        print("\n\tInforme a equação linear do problema (e.g., 1x1 + 5x2):" )
        equacao_linear = input("\n\t\t")

        coeficiente_equacaoLinear = []
        termos_equacao = re.findall(r'([+-]?\d*)x(\d+)', equacao_linear) # Corta para pegar os números, separa por + -, ? se não tiver nada

        # Itera sobre os termos encontrados na equação
        for termo in termos_equacao:
            coeficiente = termo[0] if termo[0] else '1' # Obtém o coeficiente, se presente, ou assume '1' se não houver coeficiente explícito
            coeficiente_equacaoLinear.append(float(coeficiente))

        matriz = numpy.array(coeficiente_equacaoLinear)

        if tipoDoProblema == 1:   # Se 'tipoDoProblema' for igual a 1, inverte o sinal dos coeficientes na matriz (multiplica por -1)
            matriz = matriz * -1  # Isso é no caso de ser maximização :D

        return matriz

    def calcularSolucaoBasica(self, matriz_inversa, b):
        xb = numpy.dot(matriz_inversa, b)     # multiplica as 2 matrizes   
        return xb

    def passo_2_1(self, matriz_inversa, cbt):
        λ = numpy.dot(cbt, matriz_inversa)  # multiplica as 2 matrizes
        return λ
    
    def passo_2_2(self, λ, cnt, nao_base):
        qntd_colunas = nao_base.shape[1]    #.shape[1] devolve quantas colunas sao, pra fazer o n1 n2 n3...
        lista_cnk = []
        
        for i in range (qntd_colunas):
            calculo = cnt[:, i] - numpy.dot(λ, nao_base[:, i])  # Calcula a diferença entre as colunas da matriz 'cnt' e o produto  entre λ e a coluna correspondente da matriz 'nao_base'
            lista_cnk.append(calculo.tolist()) # coloca na lista e transforma em uma lista

        return lista_cnk
    
    def passo_2_3(self, lista_cnk):

        valor_minimo = min(lista_cnk) # precisa ser uma lista pra poder fazer o min aq
        cnk = lista_cnk.index(valor_minimo) # guarda o índice de qual valor da lista foi e coloca em cnk

        return cnk, valor_minimo
    
    def passo_3(self, valor_minimo):

        if (valor_minimo[0] >= 0): # checa se o índice que está no valor mínimo entregue por cnk é maior que 0
            print("\n\t\tCnk >= 0 ⇾" + " Sim!")
            print("\n\n\t\t  A Solução ótima foi encontrada! 🎉\n\t\t. . . . . . . . . . . . . . . . . . .")
            return 1
        
        return 0
    
    def passo_4(self, matriz_inversa, cnk, nao_base):
        y = numpy.dot(matriz_inversa, nao_base[:, cnk]) # multiplica a matriz inversa pela coluna de cnk
        return y

    def passo_5(self, y, xb):

        lista_y = []
        qntd_colunas = y.shape[0]
        
        for i in range (qntd_colunas):
            if y[i] > 0: # Se for maior que 0 pode colocar no negócio
                print(f"\n\t\tY{i} <= 0? ⇾ Não!")
                lista_y.append(((xb[i])/(y[i])).tolist()) 
            else:
                print("\n\t\tY <= 0?  ⇾ Sim!")
                lista_y.append([numpy.inf]) # se for menor que 0 coloca infinito pq aí nunca vai ser o mínimo

        valor_minimo = min(lista_y)
        ε = lista_y.index(valor_minimo)

        return ε
    
    def atualizacaoDosValores(self, base, nao_base, cbt, cnt, ε, cnk, indices_variaveis):    
        coluna_base = indices_variaveis[ε]          
        coluna_nao_base = cnk

        indices_variaveis[ε] = coluna_nao_base # pega os índices pra colocar em xb

        # Trocando a coluna 0 da matrix1 com a coluna 1 da matrix2
        nao_base[:, cnk], base[:, ε] = base[:, ε].copy(), nao_base[:, cnk].copy()

        cbt[:, ε], cnt[:, cnk] = cnt[:, cnk].copy(), cbt[:, ε].copy()

        return nao_base, base, cbt, cnt, indices_variaveis

    def iteracoes(self, matriz, base, nao_base, b, cbt, cnt, copia_matrizObjetiva,  indices_variaveis):
        
        matriz_inversa = numpy.linalg.inv(base) # a inversa da base

        print("\n\tPasso 1: Cálculo da Solução Básica")
        xb = self.calcularSolucaoBasica(matriz_inversa, b)
        print(f"\n\t\tXB = |B|-1 * b =\n\t{formatacaoDaMatriz(xb)}")

        print("\n\n\tPasso 2: Cálculo dos custos relativos")

        λ = self.passo_2_1(matriz_inversa, cbt)
        λ = numpy.round(λ, 2)
        print(f"\n\t\tI) λ = CBT * |B|-1 = {λ}")

        lista_cnk = self.passo_2_2(λ, cnt, nao_base)
        print(f"\n\t\tII) Cnj= Cnj * λ * Anj = {lista_cnk}")

        cnk, valor_minimo = self.passo_2_3(lista_cnk) 
        valor_minimo = numpy.round(valor_minimo, 2)
        print("\n\t\tIII) Cnk = min {" + "Cnj}" + f" = {valor_minimo}")

        print("\n\n\tPasso 3: Teste de Otimalidade")
        if self.passo_3(valor_minimo) == 1:  
            self.solucaoOtima(indices_variaveis, xb, copia_matrizObjetiva)
            sys.exit()
        else:
            print("\n\t\tCnk >= 0 ⇾ Não! Portanto, continuamos.")

        print("\n\n\tPasso 4: Cálculo da direção do Simplex")
        y = self.passo_4(matriz_inversa, cnk, nao_base)
        print(f"\n\t\tY = |B|-1 * Ank = {y}")

        print("\n\n\tPasso 5: Verifica se o problema tem solução finita")
        ε = self.passo_5(y, xb)
        # ε = numpy.round(ε, 2)
        # print(f"\n\t\tε = min{ε}")

        nao_base, base, cbt, cnt, indices_variaveis = self.atualizacaoDosValores(base, nao_base, cbt, cnt, ε, cnk, indices_variaveis)
        
        return matriz, base, nao_base, b, cbt, cnt, indices_variaveis

    def solucaoOtima(self, indices_variaveis, xb, copia_matrizObjetiva):
        
        n = len(indices_variaveis)
        num_linhas, numero_colunas = copia_matrizObjetiva.shape         

        print("\n\n\tSolução Ótima:")
        # Primeira parte: exibir valores das variáveis básicas
        for i in range (n):
            variavel = f'x{indices_variaveis[i] + 1}'  # +1 porque os índices estão baseados em 0
            valor = xb[i][0]  # Valor em xb é uma matriz com uma coluna
            valor = numpy.round(valor, 2)
            print(f'\n\t\t{variavel} = {valor}')

        # Segunda parte: calcular e exibir o valor da função objetivo
        resultado_funcaoObjetivo = 0
        for i in range (n):
            indice_variavelAtual = indices_variaveis[i]
            
            if indice_variavelAtual < numero_colunas:  # Verifique se o índice é válido
                coeficiente = copia_matrizObjetiva[0][indice_variavelAtual]
                valor_variavel = xb[i][0]
                resultado_funcaoObjetivo += coeficiente * valor_variavel
                resultado_funcaoObjetivo = numpy.round(resultado_funcaoObjetivo, 2)
                variavel = f'x{indice_variavelAtual + 1}'  # +1 porque os índices estão baseados em 0
        
                print("\n\tSubstituindo na Função Objetiva:" 
                      + f'{coeficiente}' + " * " + f'{valor_variavel}' + " = " + f'{resultado_funcaoObjetivo}')

        print("\n\t\t\t\t    . . . . . . ." 
              + f"\n\tValor da Função Objetivo:      {resultado_funcaoObjetivo}" 
              + "\n\t\t\t\t    . . . . . . .")
        print("\n\n\t>>>  Você chegou ao fim do programa! Parabéns!\n\n\n")

if __name__ == "__main__":
    main()