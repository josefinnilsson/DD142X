# Code written by Helena Alinder & Josefin Nilsson

import matplotlib.pyplot as plt
import numpy as np
from IBP import IBP
from W import W
from Sigmoid import Sigmoid
from Obs import Observations
from GibbsSampler import sampleZW
N = 20
K = 15
alpha = 6

Z = IBP(N, alpha)
K = Z.shape[1]
W = W(0,K,0.1)

ax=plt.imshow(W,'gray',interpolation='none')
plt.tight_layout()    
plt.show()
Z, W = sampleZW(Z, alpha, W)
ax=plt.imshow(W,'gray',interpolation='none')
plt.tight_layout()    
plt.show()
