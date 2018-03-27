import numpy as np

def W(mu, K, sigma):
	W = np.zeros(shape=(K,K))
	for i in range(0,K):
		for j in range(0,K):
			w = np.random.normal(mu, sigma, K)[0]
			W[i,j] = w
	return W