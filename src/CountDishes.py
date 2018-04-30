from IBP import IBP
import numpy as np

def countDishes(N, alpha, X):
	sumOne = 0
	for x in range(X):
		Z = IBP(N, alpha)
		totOnes = np.count_nonzero(Z == 1)
		sumOne += (totOnes/N)
	return (sumOne/X)