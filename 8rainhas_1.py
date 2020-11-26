"""
Você deve resolver o clássico exercício das 8 rainhas
Nele o usuário lhe passa o tamanho do tabuleiro n
(lembrar que tabuleiros são quadrados então o usuário
só precisa lhe passar um inteiro) e você deve gerar
uma todas as distribuições de n rainhas neste tabuleiro
e imprimi-las de uma forma adequada.

Veja o livro Beginning Python, na descrição
do video para a explicação da solução, ou entre
no dropbox para ver a solução comentada

Esse exercício não é fácil!!
Não se preocupe se você não conseguir.
"""

from math import fabs
import pdb

def Tabuleiro(lado=0):
	# Cria uma lista com '.' como uma base. E as insere em outras listas.
    return [list('.'*lado) for l in range(0, lado**2) if l % lado == 0]


def Atk_Trail(x, y, Tabuleiro):
	
	def subst(x, y, elemento):
		nonlocal tab
		
		if tab[y][x] not in ['•', '♥']:
		
			# Apaga o elemento e insere o '•'
			tab[y].pop(x)
			tab[y].insert(x, elemento)
				
	tab = Tabuleiro.copy()

	tab[y].pop(x)
	tab[y].insert(x, '♥')
	
	# Para a vertical e horizontal e linhas cruzadas
	
	for iy, ey in iter(enumerate(tab)):
		for ix, ex in iter(enumerate(ey)):
    		
			
			subx, suby = x-ix, y-iy
			
			if suby < 0:
				suby *= -1
			if subx < 0:
				subx *= -1

			#    Diagonal      Vertical e Horizontal
			if (subx == suby) or (iy == y or ix == x) and ex != '♥':
				subst(ix, iy, '•')

			# (iy == y or ix == x) Se estiver ao lado, ou acima da rainha ou
			# (subx == suby) Se o módulo da amplitude for igual
			# Ele cria uma trail com o '•'

	return tab

def percorre(tabuleiro, px=0, py=0):
	
	size = len(tabuleiro)

	pdb.set_trace()

	ptab1 = Atk_Trail(px, py, tabuleiro.copy()).copy()
	ptab2 = Atk_Trail(px, int(fabs(py-size+1)), tabuleiro.copy()).copy()
	ntab1 = Atk_Trail(int(fabs(px-size+1)), py, tabuleiro.copy()).copy()
	ntab2 = Atk_Trail(int(fabs(px-size+1)), int(fabs(py-size+1)), tabuleiro.copy()).copy()	

	for ey in range(size):

		for ex in range(size):
			
			if ptab1[ey][ex] not in ['•', '♥']:
				ptab1 = Atk_Trail(ex, ey, ptab1).copy()
			
			if ptab2[int(fabs(ey-size+1))][ex] not in ['•', '♥']:
				ptab2 = Atk_Trail(ex, int(fabs(ey-size+1)), ptab2).copy()

			if ntab1[ey][int(fabs(ex-size+1))] not in ['•', '♥']:
				ntab1 = Atk_Trail(int(fabs(ex-size+1)), ey, ntab1).copy()

			if ntab2[int(fabs(ey-size+1))][int(fabs(ex-size+1))] not in ['•', '♥']:
				ntab2 = Atk_Trail(int(fabs(ex-size+1)), int(fabs(ey-size+1)), ntab2).copy()

	return ptab1, ptab2, ntab1, ntab2

        
def main():
	size = int(input('Tamanho do lado do tabuleiro: '))
	
	# Isso é uma lista de possibilidades.
	possibilidades = []
	
	# Ele percorre todas as maneiras de iniciar o tabuleiro possíveis.
	for iy in range(size):
		for ix in range(size):


			tentativas = percorre(Tabuleiro(size).copy(), ix, iy)
			for resultado in tentativas:	
				cont = 0

				for l in resultado:

					if '♥' in l:
						cont += l.count('♥')
			

				# Se essa contagem de rainhas (o "♥") for exatamente igual ao tamanho
				# ele adiciona as possibilidades viáveis.
				if cont == size and resultado not in possibilidades:
					possibilidades.append(resultado)
			

	
	# Aqui ele percorre os tabuleiros que foram armazenados.
	for indice, tabuleiros in enumerate(possibilidades):

		print('POSSIBILIDADE No.%i' %(indice+1))
		cont = 0
		
		for layers in tabuleiros:
			
			print(layers)
			if '♥' in layers:
				cont += layers.count('♥')
		print('\n')
		print(cont)
		print('\n')

main()
	
