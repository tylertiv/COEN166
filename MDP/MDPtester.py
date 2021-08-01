#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 12:28:17 2020

@author: tylertivadar
"""

import MarkovDecisionUtil as mdp
import numpy as np

T=np.zeros((5,5,2),dtype=float) # SxSxA
R=np.zeros((5,5,2),dtype=float) # SxSxA

# s0: cool; s1: warm; s3: overheated

                               # T[:,:,0]
# a1;                          #       s1   s2   s3   s4   s5
T[:,:,0]=[[0, 0.5, 0.5, 0, 0], #   s1   0  0.5  0.5    0    0
          [0, 0, 0, 0.5, 0.5], #   s2   0    0    0  0.5  0.5
          [0, 0, 0, 0.9, 0.1], #   s3   0    0    0  0.9  0.1
          [0, 0, 0, 1, 0],     #   s4   0    0    0    1    0
          [0, 0, 0, 0, 1]]     #   s5   0    0    0    0    1
                               
                               

                               # R[:,:,0]
# a1;                          #       s1   s2   s3   s4   s5
R[:,:,0]=[[0, 0, 0, 0, 0],     #   s1   0    0    0    0    0
          [0, 0, 0, 1, 1],     #   s2   1    1    1    1    1
          [0, 0, 0, 0, 0],     #   s3   0    0    0    0    0
          [0, 0, 0, 0, 0],     #   s4   0    0    0    0    0
          [0, 0, 0, 0, 1]]     #   s5   1    1    1    1    1
                              
                              
                               # T[:,:,1]
# a2;                          #       s1   s2   s3   s4   s5
T[:,:,1]=[[0, 0.9, 0.1, 0, 0], #   s1   0  0.9  0.1    0    0
          [0, 0, 0, 0.9, 0.1], #   s2   0    0    0  0.9  0.1
          [0, 0, 0, 0.5, 0.5], #   s3   0    0    0  0.5  0.5
          [0, 0, 0, 1, 0],     #   s4   0    0    0    1    0
          [0, 0, 0, 0, 1]]     #   s5   0    0    0    0    1     
                               
                               

                               # R[:,:,1]
# a1;                          #       s1   s2   s3   s4   s5
R[:,:,1]=[[0, 0, 0, 0, 0],     #   s1   0    0    0    0    0
          [0, 0, 0, 1, 1],     #   s2   1    1    1    1    1
          [0, 0, 0, 0, 0],     #   s3   0    0    0    0    0
          [0, 0, 0, 0, 0],     #   s4   0    0    0    0    0
          [0, 0, 0, 0, 1]]     #   s5   1    1    1    1    1
gamma=0.9
epsilon = 1e-4

V1 = mdp.value_iteration(T, R, gamma, epsilon)


T=np.zeros((3,3,2),dtype=float) # SxSxA
R=np.zeros((3,3,2),dtype=float) # SxSxA

                               # T[:,:,0]
# a0=do not spin;              #       s0  s1  s2
T[:,:,0]=[[1,0,0],             #   s0   1   0   0
          [1,0,0],             #   s1   1   0   0
          [0,1,0]]             #   s2   0   1   0

                               # R[:,:,0]
                               #       s0  s1  s2
R[:,:,0]=[[0,0,0],             #   s0   0   0   0
          [3,0,0],             #   s1   3   0   0
          [0,3,0]]             #   s2   0   3   0

                               # T[:,:,1]
# a1=fast                      #       s0  s1  s2               
T[:,:,1]=[[0,1,0],             #   s0   0   1   0             
          [0,0,1],             #   s1   0   0   1                 
          [0,0,1]]             #   s2   0   0   1       

                               # R[:,:,1]
                               #       s0  s1  s2
R[:,:,1]=[[0,-1,0],            #   s0   0  -1   0
          [0,0,2],             #   s1   0   0   2
          [0,0,2]]             #   s2   0   0   2

max_iteration = 2000
gamma = 0.8
epsilon = 1e-4

V2 = mdp.value_iteration(T, R, gamma, epsilon)

T=np.zeros((3,3,2),dtype=float) # SxSxA
R=np.zeros((3,3,2),dtype=float) # SxSxA

                               # T[:,:,0]
# a0=do not spin;              #       s0  s1  s2
T[:,:,0]=[[1,0,0],             #   s0   1   0   0
          [.4,.6,0],             #   s1  .4  .6   0
          [.4,0,.6]]             #   s2   0  .4  .6

                               # R[:,:,0]
                               #       s0  s1  s2
R[:,:,0]=[[0,0,0],             #   s0   0   0   0
          [3,3,0],             #   s1   3   0   0
          [3,0,3]]             #   s2   0   3   0

                               # T[:,:,1]
# a1=fast                      #       s0  s1  s2               
T[:,:,1]=[[.7,.3,0],             #   s0  .7  .3   0             
          [0,.7,.3],             #   s1   0  .7  .3                
          [0,0,1]]             #   s2   0   0   1       

                               # R[:,:,1]
                               #       s0  s1  s2
R[:,:,1]=[[-1,-1,0],            #   s0   0  -1   0
          [0,2,2],             #   s1   0   0   2
          [0,0,2]]             #   s2   0   0   2

max_iteration = 2000
gamma = 0.8
epsilon = 1e-4

V3 = mdp.value_iteration(T, R, gamma, epsilon)
