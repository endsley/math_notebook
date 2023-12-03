#!/usr/bin/env python
import numpy as np


def eigh_sort(Q):	# From largest eig to smallest
	[D,V] = np.linalg.eigh(Q)
	idx = D.argsort()[::-1]   
	eigenValues = D[idx]
	eigenVectors = V[:,idx]
	return [eigenValues, eigenVectors]


