# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 12:05:20 2020

@author: tylertivadar
"""

import numpy as np

def value_iteration(T, R, gamma, epsilon, max_iteration=2000):
    V=np.zeros((len(T),max_iteration+1),dtype=float) # V: 5 x (max_iteration+1)
    threshold = epsilon*(1-gamma)/gamma
    k = 0
    for k in range(max_iteration):
        for s in range(len(T)):                  #find V values for each state
            sums = []
            for a in range(len(T[s,0])):    #find sum of s' for each action
                tmp = 0
                for sprime in range(len(T[s])):
                    tmp += T[s, sprime, a]*(R[s, sprime, a]+gamma*V[sprime, k])
                sums.append(tmp)
            V[s, k+1] = np.max(sums)
        if np.max(np.abs(V[:,k+1]-V[:,k])) <= threshold:
            print("Threshold reached at k = ", k)
            for i in range(3):
                print(np.max(V[:,k+1]-V[:,k]))
            break
    return V
        

