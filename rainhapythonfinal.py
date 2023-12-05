class desafio():
    def __init__(self, tamanho=8):
        self.simbolos = [".", "*", "Q"]
        self.tamanho = tamanho

        self.resultados = self.montaTestes()

    def criaTabuleiro(self, tamanho):
        tabuleiro = []
        for y in range(tamanho):
            linha = []
            for x in range(tamanho):
                linha.append(self.simbolos[0])

            tabuleiro.append(linha[:])

        return tabuleiro[:][:]
            
    def colocaDama(self, tabuleiroOriginal, posicoes):
        tabuleiroCopia = [linha[:] for linha in tabuleiroOriginal] 

        def substitui(listaComposta, posicaoSubstituicao, novoConteudo):
            listaComposta[posicaoSubstituicao[1]].pop(posicaoSubstituicao[0])
            listaComposta[posicaoSubstituicao[1]].insert(posicaoSubstituicao[0], novoConteudo)

            return listaComposta

        for posicao in posicoes:
            # RETORNA FALSO, LOCALIZAÇÃO DE DAMA INVÁLIDA
            for y in range(len(tabuleiroCopia)):
                distanciaY = posicao[1] - y
                if distanciaY < 0: distanciaY *= -1

                for x in range(len(tabuleiroCopia)):
                    distanciaX = posicao[0] - x
                    if distanciaX < 0: distanciaX *= -1

                    if tabuleiroCopia[y][x] == self.simbolos[0]:                 
                        if y == posicao[1]: 
                            tabuleiroCopia = substitui(tabuleiroCopia, (x, y), self.simbolos[1])

                        if x == posicao[0]:
                            tabuleiroCopia = substitui(tabuleiroCopia, (x, y), self.simbolos[1])

                        if distanciaY == distanciaX:
                            tabuleiroCopia = substitui(tabuleiroCopia, (x, y), self.simbolos[1])

                    # Sem necessidade, já ocorre a filtração dos resultados errados no checaPosicao
                    """elif tabuleiroCopia[y][x] == self.simbolos[2] and (y == posicao[1] or x == posicao[0] or distanciaY == distanciaX):
                        return False"""

            # COLOCA A DAMA
            tabuleiroCopia = substitui(tabuleiroCopia[:][:], posicao, self.simbolos[2])

        return [linha[:] for linha in tabuleiroCopia]

    def checaPosicao(self, posicoesDamas):
        
        for posicao in posicoesDamas:
            for y in range(self.tamanho):
                distanciaY = posicao[1] - y
                if distanciaY < 0: distanciaY *= -1

                for x in range(self.tamanho):
                    distanciaX = posicao[0] - x
                    if distanciaX < 0: distanciaX *= -1

                    # RETORNA FALSO, LOCALIZAÇÃO DE DAMA INVÁLIDA
                    if (distanciaX > 0 or distanciaY > 0):
                        if (x, y) in posicoesDamas and (y == posicao[1] or x == posicao[0] or distanciaY == distanciaX):
                            return False

        
        return True

    def montaTestes(self):
        validos = []
        resultadosTransitorios = []

        for y in range(self.tamanho//2):
            for x in range(self.tamanho//2):
                resultadosTransitorios.append([(x, y)])

                for repeticoes in range(self.tamanho - 1):
                    validosTransitorios = []

                    for posicaoTeste in resultadosTransitorios:
                        posicoesPossiveisX = tuple(set(range(self.tamanho)) - set(posicao[0] for posicao in posicaoTeste))
                        posicoesPossiveisY = tuple(set(range(self.tamanho)) - set(posicao[1] for posicao in posicaoTeste))
                
                        if len(posicoesPossiveisY) > 0 and len(posicoesPossiveisX) > 0:
                            for indiceLinha in posicoesPossiveisY:
                                for indiceColuna in posicoesPossiveisX:
                                    if (indiceColuna, indiceLinha) not in posicaoTeste:
                                        posicaoSimulada = list(posicaoTeste + [(indiceColuna, indiceLinha)])[:][:]
                                        posicaoSimulada.sort()

                                        if posicaoSimulada not in validosTransitorios:
                                            if self.checaPosicao(posicaoSimulada) == True:
                                                validosTransitorios.append(posicaoSimulada)
                                
                    resultadosTransitorios = validosTransitorios[:][:]

                print("POSICAO INICIAL (" + str(x) + ", " + str(y) + ") TOTALMENTE SIMULADA")
            
                validos += self.filtraRepeticao(resultadosTransitorios)
        
        print("COLOCANDO OS RESULTADOS EM TABULEIROS")

        tabuleiros = []
        for posicoes in self.filtraRepeticao(validos):
            tabuleiros.append(self.colocaDama(self.criaTabuleiro(8), posicoes))

        return tabuleiros

    def filtraRepeticao(self, lista):
        valoresUnicos = []

        while len(lista) > 0:
            if lista[0] not in valoresUnicos:
                valoresUnicos.append(lista[0][:][:])
            
            lista.pop(0)

        return valoresUnicos[:][:]



# ===================================

resultados = 0
for tabuleiro in desafio(8).resultados:
    resultados += 1
    print("SOLUÇÃO", resultados, ":")

    for linha in tabuleiro:
        print(linha)

    print()
print(resultados)