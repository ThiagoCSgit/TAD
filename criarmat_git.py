def criamat():
	mat = []
	qlin = int(input('Quantidade de linhas da matriz: '))
	qcol = int(input('Quantidade de colunas da matriz: '))
	for i in range(qlin):
		mat.append([])
		for j in range(qcol):
			mat[i][j].append(int(input('Digite os valores da matriz: ')))
	return mat
	

x = criamat()
