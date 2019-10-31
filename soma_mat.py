#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  soma_mat.py
#
def somar(matA, matB):
	soma = []
	for i in range(matA):
		soma.append([])
		for j in range(matA[i]):
			if (len(matA) == len(matB)) and (len(matA[i]) == len(matB[i])):
				soma[i][j].append(matA[i][j] + matB[i][j]) 
				return soma
	else:
		return 'Não é possível realizar a soma, as matrizes não são de mesma ordem!!'
		
x = somar(matA,matB)
