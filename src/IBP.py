# Code from Github user @sld42 https://github.com/sld42

import numpy as np
def IBP(N, alpha):
   #Generate initial number of dishes from a Poisson
    n_init = np.random.poisson(alpha,1)
    Z = np.zeros(shape=(N,n_init[0]))
    Z[0,:] = 1
    m = np.sum(Z,0)
    K = n_init[0]
    for i in range(0,N):
        #Calculate probability of visiting past dishes
        prob = m/(i+1)
        index = np.greater(prob,np.random.rand(1,K))
        Z[i,:] = index.astype(int);
        #Calculate the number of new dishes visited by customer i
        knew = np.random.poisson(alpha/(i+1),1)[0]
        Z=np.concatenate((Z,np.zeros(shape=(N,knew))), axis=1)
        Z[i,K:K+knew:1] = 1
        #Update matrix size and dish popularity count
        K = K+knew
        m = sum(Z,0)    
    return Z