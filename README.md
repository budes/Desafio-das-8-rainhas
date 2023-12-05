# Desafio-das-8-rainhas
Esse repositório hospeda um script que executa o desafio das 8 damas.

## Modo de solução aplicado
Simulação de posições iniciais para produzir todas as possibilidades possíveis a partir disso

### Como funciona? 
(Linha 80)
```
for y in range(self.tamanho//2):
    for x in range(self.tamanho//2):
        resultadosTransitorios.append([(x, y)])
```
Define uma posição inicial para trabalhar. Fiz com metade do tabuleiro, porque os resultados gerados por simular ele inteiramente seriam redundantes.

A partir dessa posição inicial, ele define todas as possibilidades existentes a partir dela

```
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
```
Filtra repetições a partir dessa inicial, adicionando ao validosTransitorios, antes de adicionar aos resultadosTransitorios. Faço isso para diminuir o volume de dados analisados e acelerar a velocidade de processamento.

### Alguns sistemas e sua importância e suas particularidades
Recursos usados para garantir o funcionamento desse script.

#### checaPosicao e colocaDama
Ambos se parecem muito, mas se diferenciam no seguinte.

Enquanto o checaPosicao calcula, o colocaDama visualiza.

A importância do checaPosicao é que ele garante uma maior velocidade da analise dos dados e garante que a posicao seja valida.

Agora o colocaDama serve para fazer o tabuleiro aparecer, ele poderia ser usado no lugar do checaPosicao com alguams alterações, mas sua velocidade comprometeria o funcionamento do código.

#### filtraRepeticao
Como o próprio nome aponta, serve para filtrar as repetições do código. O que entra em destaque nele é que seu funcionamento só é possível pelo .sort(), por causa da maneira como o próprio python compara listas.
A utilização de um algoritmo de organização dificulta a eficiência dessa parte, por isso, uma outra maneira de estruturar seria aplicando um algoritmo de organização dentro do próprio método.

O dilema desse filtraRepeticao foi justamente esse, o que me deixou meio intrigado com uma solução como essa para testar no futuro, provavelmente vou testar depois, mesmo que não coloque no github.
