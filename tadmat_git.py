#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  TAD_matriz.py
#  
#  Copyright 2019 20191bsi0271 <20191bsi0271@SR6161>

def criar(qlin,qcol):
	mat = {'lin' : qlin, 'col' : qcol}
	return mat

def setIJ(tad_mat,i,j,valor):
	if valor != 0:
		if i >= 1 and i <= tad_mat['lin'] and j >= 1 and j <= tad_mat['col']:
			tad_mat[(i,j)] = valor
			return tad_mat
		else:
			print('A posição não existe!')
	else:
		return tad_mat



def getIJ(tad_mat,i,j):
	if i >= 1 and i <= tad_mat['lin'] and j >= 1 and j <= tad_mat['col']:
		if (i,j) in tad_mat:
			 return tad_mat[(i,j)] 
		else:
			return 0
	else:
		print('Posição inexistente!')

def somar(tad_matA, tad_matB):
	if (tad_matA['lin'] == tad_matB['lin']) and (tad_matA['col'] == tad_matB['col']):
		tad_matC = criar(tad_matA['lin'], tad_matA['col'])
		for i in range(1,tad_matA['lin'] + 1):
			for j in range(1,tad_matA['col'] + 1):
				soma = getIJ(tad_matA,i,j) + getIJ(tad_matB,i,j)
				setIJ(tad_matC,i,j,soma)
		return tad_matC
	else:
		return 'Não é possível realizar a soma, as matrizes não são de mesma ordem!!'

def paraStr(tad):
	s_mat = ''
	for i in range(1,tad['lin'] + 1):
		for j in range(1,tad['col'] + 1):
			if (i,j) in tad:
				s_mat += str(tad[(i,j)]) + '   '
			else:
				s_mat += '0' + '   '
		s_mat += '\n'
	return s_mat

def mat_trans(tad_mat):
	mat_trans = {'lin' : tad_mat['col'], 'col' : tad_mat['lin']}
	for i in range(1, tad_mat['col'] + 1):
		for j in range(1, tad_mat['lin'] + 1):
			mat_trans[(i,j)] = tad_mat[(j,i)]
	return mat_trans

def main():
	matrizA = criar(2, 2)
	matrizB = criar(2, 2)
	for i in range(1, 3):
		for j in range(1, 3):
			matrizA = setIJ(matrizA, i, j, int(input('Digite um valor para matrizA: ')))
	for i in range(1, 3):
		for j in range(1, 3):
			matrizB = setIJ(matrizB, i, j, int(input('Digite um valor para matrizB: ')))
	tad_soma = somar(matrizA,matrizB)
	print('Matriz A:\n{}'.format(paraStr(matrizA)))
	print('Matriz B:\n{}'.format(paraStr(matrizB)))
	print('Soma das matrizes:\n{}'.format(paraStr(tad_soma)))
	print('Transposta da matriz A:\n{}'.format(paraStr(mat_trans(matrizA))))
	print('Transposta da matriz B:\n{}'.format(paraStr(mat_trans(matrizB))))
	return 0
if __name__ == '__main__':	
	main()
