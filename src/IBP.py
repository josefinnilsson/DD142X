# Code from Github user @sld42 https://github.com/sld42

import numpy as np
def IBP(N, alpha):
   #Generate initial number of dishes from a Poisson
    n_init = np.random.poisson(alpha)
    Z = np.zeros(shape=(N,n_init))
    Z[0,:] = 1
    m = np.sum(Z,0)
    K = n_init
    for i in range(1,N):
        #Calculate probability of visiting past dishes
        prob = m/(i + 1)
        index = np.greater(prob,np.random.rand(1,K))
        Z[i,:] = index.astype(int);
        #Calculate the number of new dishes visited by customer i
        new = np.random.poisson(alpha/(i + 1))
        Z=np.concatenate((Z,np.zeros(shape=(N,new))), axis=1)
        Z[i,K:K+new:1] = 1
        #Update matrix size and dish popularity count
        K = K+new
        m = sum(Z,0)
    return Z