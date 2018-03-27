# Code written by Helena Alinder & Josefin Nilsson

import matplotlib.pyplot as plt
import numpy as np
from IBP import IBP
from W import W
from Sigmoid import Sigmoid
N = 10
K = 20

W = W(0,K,0.1)
Z = IBP(N,K)
Y = np.empty(shape=(N,N))
print "first Y"
ax=plt.imshow(Y,'gray',interpolation='none')
plt.tight_layout()    
plt.show() 
print Y;
x = 0;
for i in range(0,N):
	for j in range(0,N):
		for k in range(0,K):
			for kp in range(0,K):
				x += (Z[i,k]*Z[j,kp]*W[k,kp])
		sigma = Sigmoid(x)
		rand = np.random.uniform(0,1)
		if (sigma > rand):
			Y[i,j] = 1
		else:
			Y[i,j] = 0
		x = 0;
print "second Y"
ax=plt.imshow(Y,'gray',interpolation='none') 
plt.tight_layout()    
plt.show()
print Y
