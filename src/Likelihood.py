from Sigmoid import Sigmoid
def Likelihood(Z, W, i, k, row):
	N = Z.shape[0]
	K = Z.shape[1]
	KW = W.shape[1]
	x = 0
	for j in range(0,N):
		for kp in range(0,K):
			x += (Z[i,k] * Z[j,kp] * W[k,kp])
	return x