# Code written by Helena Alinder & Josefin Nilsson

import numpy as np

def Sigmoid(x):
	sigma = 1/(1 + np.exp(-x))
	return sigma