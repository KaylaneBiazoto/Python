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

    metodo = Metodo_do_simplex()

    matriz_funcaoObjetiva = (metodo.primeiraEquivalencia()).reshape(1, -1)
    
    copia_matrizObjetiva = numpy.copy(matriz_funcaoObjetiva)

    qntd_restricoes, qntd_variaveisDecisao = metodo.informacoesDasRestricoes()
    
    matriz, base, nao_base, b, cbt, cnt, indices_variaveis = metodo.criarMatriz(qntd_restricoes, qntd_variaveisDecisao, matriz_funcaoObjetiva) 

    for i in range (qntd_restricoes + 1):
        if i > (qntd_restricoes + 1):
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

                    metodo = self.funcaoObjetiva(tipoDoProblema)
                    
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
        
        matriz = numpy.zeros((qntd_variaveisDecisao, qntd_variaveisDecisao + qntd_restricoes))
        b = numpy.zeros((qntd_variaveisDecisao, 1))

        base = numpy.zeros((qntd_variaveisDecisao, qntd_variaveisDecisao))          
        nao_base = numpy.zeros((qntd_variaveisDecisao, qntd_restricoes))

        cbt = numpy.zeros ((1, qntd_variaveisDecisao))
        cnt = matriz_funcaoObjetiva

        indices_variaveis = []

        for linha_atual in range (qntd_variaveisDecisao):
            matriz, base, nao_base, b, cbt, indices_variaveis = self.processamentoDeUmaLinha(matriz, base, nao_base, b, cbt, linha_atual, qntd_restricoes, indices_variaveis) 

        return matriz, base, nao_base, b, cbt, cnt, indices_variaveis

    def processamentoDeUmaLinha(self, matriz, base, nao_base, b, cbt, linha, qntd_restricoes, indices_variaveis):
        print("\n\tInforme os valores das restrições:")

        for coluna in range (qntd_restricoes):
            valor = self.getValorDaMatriz(linha, coluna)          
            matriz[linha, coluna] = valor
            nao_base[linha, coluna] = valor

        operador = self.getOperadorCondicional()
        
        if operador == '<=':
            matriz[linha, qntd_restricoes + linha] = 1
            base[linha, linha] = 1
            indices_variaveis.append(qntd_restricoes + linha)
        elif operador == '>=':
            matriz[linha, qntd_restricoes + linha] = -1
            base[linha, linha] = -1
            indices_variaveis.append(qntd_restricoes + linha)  
        else:
            terminateProgram()

        valor_inequacao = self.getValorDaComparacao()          

        if valor_inequacao < 0:
            matriz[linha] = matriz[linha] * -1
            b[linha, 0] = valor_inequacao * -1
            cbt[0] = 0
        else:
            b[linha, 0] = valor_inequacao
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
        termos_equacao = re.findall(r'([+-]?\d*)x(\d+)', equacao_linear)

        for termo in termos_equacao:
            coeficiente = termo[0] if termo[0] else '1'
            coeficiente_equacaoLinear.append(float(coeficiente))

        matriz = numpy.array(coeficiente_equacaoLinear)

        if tipoDoProblema == 1:
            matriz = matriz * -1

        return matriz

    def calcularSolucaoBasica(self, matriz_inversa, b):
        xb = numpy.dot(matriz_inversa, b)        
        return xb

    def passo_2_1(self, matriz_inversa, cbt):
        λ = numpy.dot(cbt, matriz_inversa)
        return λ
    
    def passo_2_2(self, λ, cnt, nao_base):
        qntd_colunas = nao_base.shape[1]
        lista_cnk = []
        
        for i in range (qntd_colunas):
            calculo = cnt[:, i] - numpy.dot(λ, nao_base[:, i])
            lista_cnk.append(calculo.tolist())

        return lista_cnk
    
    def passo_2_3(self, lista_cnk):

        valor_minimo = min(lista_cnk)
        cnk = lista_cnk.index(valor_minimo)

        return cnk, valor_minimo
    
    def passo_3(self, valor_minimo):

        if (valor_minimo[0] >= 0):
            print("\n\t\tCnk >= 0 ⇾" + " Sim!")
            print("\n\n\t\t  A Solução ótima foi encontrada! 🎉\n\t\t. . . . . . . . . . . . . . . . . . .")
            return 1
        
        return 0
    
    def passo_4(self, matriz_inversa, cnk, nao_base):
        y = numpy.dot(matriz_inversa, nao_base[:, cnk])
        return y

    def passo_5(self, y, xb):
        lista_y = []
        qntd_colunas = y.shape[0]
        
        for i in range (qntd_colunas):
            if y[i] > 0:
                print(f"\n\t\tY{i} <= 0? ⇾ Não!")
                lista_y.append(((xb[i])/(y[i])).tolist()) 
            else:
                print("\n\t\tY <= 0?  ⇾ Sim!")
                lista_y.append([numpy.inf])

        valor_minimo = min(lista_y)
        ε = lista_y.index(valor_minimo)

        return ε
    
    def atualizacaoDosValores(self, base, nao_base, cbt, cnt, ε, cnk, indices_variaveis):    
        coluna_base = indices_variaveis[ε]          
        coluna_nao_base = cnk

        indices_variaveis[ε] = coluna_nao_base

        nao_base[:, cnk], base[:, ε] = base[:, ε].copy(), nao_base[:, cnk].copy()

        cbt[:, ε], cnt[:, cnk] = cnt[:, cnk].copy(), cbt[:, ε].copy()

        return nao_base, base, cbt, cnt, indices_variaveis

    def iteracoes(self, matriz, base, nao_base, b, cbt, cnt, copia_matrizObjetiva,  indices_variaveis):
        
        matriz_inversa = numpy.linalg.inv(base)

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
        print("\n\t\tε = min{" + f"{ε}" +"}")

        nao_base, base, cbt, cnt, indices_variaveis = self.atualizacaoDosValores(base, nao_base, cbt, cnt, ε, cnk, indices_variaveis)
        
        return matriz, base, nao_base, b, cbt, cnt, indices_variaveis

    def solucaoOtima(self, indices_variaveis, xb, copia_matrizObjetiva):
        n = len(indices_variaveis)
        num_linhas, numero_colunas = copia_matrizObjetiva.shape         

        print("\n\n\tSolução Ótima:")

        for i in range (n):
            variavel = f'x{indices_variaveis[i] + 1}'  
            valor = xb[i][0]
            valor = numpy.round(valor, 2)
            print(f'\n\t\t{variavel} = {valor}')

        resultado_funcaoObjetivo = 0
        for i in range (n):
            indice_variavelAtual = indices_variaveis[i]
            
            if indice_variavelAtual < numero_colunas: 
                coeficiente = copia_matrizObjetiva[0][indice_variavelAtual]
                valor_variavel = xb[i][0]
                resultado_funcaoObjetivo += coeficiente * valor_variavel
                resultado_funcaoObjetivo = numpy.round(resultado_funcaoObjetivo, 2)
                variavel = f'x{indice_variavelAtual + 1}'  
        
                print("\n\tSubstituindo na Função Objetiva:" 
                      + f'{coeficiente}' + " * " + f'{valor_variavel}' + " = " + f'{resultado_funcaoObjetivo}')

        print("\n\t\t\t\t    . . . . . . ." 
              + f"\n\tValor da Função Objetivo:      {resultado_funcaoObjetivo}" 
              + "\n\t\t\t\t    . . . . . . .")
        print("\n\n\t>>>  Você chegou ao fim do programa! Parabéns!\n\n\n")

if __name__ == "__main__":
    main()