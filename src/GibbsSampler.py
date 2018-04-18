import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as SPST
from Likelihood import Likelihood
from probLikelihood import probLikelihood
from Sigmoid import Sigmoid

def sampleZW(Z, alpha, W):
	N = Z.shape[0]
	K = Z.shape[1]
	m = sum(Z,0)
	for k in range (0,5):
		for i in range (0,N):
			K = Z.shape[1]
			row = Z[i]
			Z = np.delete(Z, i, 0)
			m = sum(Z,0) 
			Z = np.append(Z,np.zeros(shape=(1,K)), axis=0)
			zeroColumns = [ki for ki in range(0,K) if m[ki] == 0]
			for j in range (0, K):
				K = Z.shape[1]
				if m[j] > 0:
					Z[i,k] = 1
					probzikone = m[j]/N * Likelihood(Z, W, i, j, row)
					Z[i,k] = 0
					probzikzero = (N - m[j])/N * Likelihood(Z, W, i, j, row)
					sigma = Sigmoid(-(probzikone - probzikzero))
					rand = np.random.uniform(0,1)
					if (sigma > rand):
						Z[N - 1,j] = 0
					else:
						Z[N - 1,j] = 1
			for i in range(0,len(zeroColumns)):
				Z = np.delete(Z, zeroColumns[i],1)
				W = np.delete(W, zeroColumns[i], 0)
				W = np.delete(W, zeroColumns[i], 1)
			K = Z.shape[1]
			pois = float(alpha)/float(N)
			knew = np.random.poisson(pois)
			kold = len(zeroColumns)
			Znew = Z
			Znew = np.concatenate((Z,np.zeros(shape=(N,knew))), axis=1)
			Znew[i,K:K+knew:1] = 1
			kdiff = float(knew) - float(kold)
			if kdiff > 0:
				knew = knew - kold
				Wnew = probW(knew, W)
				probNew = probLikelihood(Znew, Wnew, i)
				probOld = probLikelihood(Z, W, i)
				probQuota = float(probNew)/float(probOld)
				rand = np.random.uniform(0,1);
				if (probQuota >= rand):
					Z = Znew
					W = sampleW(W, Wnew)
			kold = 0
	return Z, W

def probW (Knew, W):
	K = W.shape[0]
	W = np.concatenate((W, np.zeros(shape=(K, Knew))), axis=1)
	W = np.append(W, np.zeros(shape=(Knew, K+Knew)), axis=0)
	return W

def sampleW (W, Wnew):
	K = W.shape[0]
	for k in range(0,K):
		for kp in range(0,K):
			mu = W[k,kp]
			w = np.random.normal(mu, 0.1, K)[0]
			Wnew[k,kp] = w
	Knew = Wnew.shape[0]
	for k in range(K, Knew):
		for kp in range(K, Knew):
			w = np.random.normal(mu, 0.1, Knew)[0]
			Wnew[k,kp] = w
	return Wnew
