from IBP import IBP

def count(N, alpha, X):
	sumC = 0
	for x in range(X):
		clusters = []
		Z = IBP(N, alpha)
		for i in range(Z.shape[0]):
			tmp = []
			for j in range(len(Z[i])): 	
				if Z[i][j] == 1:
					tmp.append(j)
			if not tmp in clusters:
				clusters.append(tmp)
		sumC += len(clusters)
	return (sumC/X)