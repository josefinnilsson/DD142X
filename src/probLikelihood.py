import numpy as np

from Sigmoid import Sigmoid

def probLikelihood (Z, W, i):
	N = Z.shape[0]
	K = Z.shape[1]
	totLikelihood = 1
	x = 0
	for j in range(0,N):
		for k in range(0,K):
			for kp in range(0,K):
				x += (Z[i,k]*Z[j,kp]*W[k,kp])
				# print x 
			sigma = Sigmoid(x)
			totLikelihood += np.log(sigma)
	return totLikelihood