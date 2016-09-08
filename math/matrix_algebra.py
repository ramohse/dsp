# Matrix Algebra
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 18:26:06 2016

@author: ramohse

Defines matrices and vectors and uses Python/numpy to check the hand-written
work done on linear algebra
"""

import numpy as np

A = np.matrix([[1, 2, 3], [2, 7, 4]])
B = np.matrix([[1, -1], [0, 1]])
C = np.matrix([[5, -1], [9, 1], [6, 0]])
D = np.matrix([[3, -2, -1], [1, 2, 3]])
u = np.array([6, 2, -3, 5])
v = np.array([3, 5, -1, 4])
w = np.array([[1], [8], [0], [5]])


### 06.01 Matrix Dimensions

## 06.01.01
#print('1.1) ', A.shape)
# (2, 3)

## 06.01.02
#print('1.2) ', B.shape)
# (2, 2)

## 06.01.03
#print('1.3) ', C.shape)
# (3, 2)

## 06.01.04
#print('1.4) ', D.shape)
# (2, 3)

## 06.01.05
#print('1.5) ', u.shape)
# (4,)

## 06.01.06
#print('1.6) ', w.shape)
# (4, 1)
#print('\n')


### 06.02 Vector Operations

## 06.02.01
#ans0201 = u + v
#rint('2.1) ', ans0201)
# [9, 7, -4, 9]

## 06.02.02
#ans0202 = u - v
#print('2.2) ', ans0202)
# [3, -3, -2, 1]

## 06.02.03
#ans0203 = 6 * u
#print('2.3) ', ans0203)
# [36, 12, -18, 30]

## 06.02.04
#ans0204 = np.dot(u, v)
#print('2.4) ', ans0204)
# 51

## 06.02.05
#ans0205 = np.linalg.norm(u)
#print('2.5) ', ans0205)
# 8.602325
#print('\n')


### 06.03 Matrix Operations

## 06.03.01
#ans0301 = A + C
#print('3.1) ', ans0301)
# not defined

## 06.03.02
#ans0302 = A + C.T
#print('3.2) ', ans0302)
# [[6, 11, 9]
#  [1, 8, 4]]

## 06.03.03
#ans0303 = C.T + (3 * D)
#print('3.3) ', ans0303)
# [[14, 3, 3]
#  [2, 7, 9]]

## 06.03.04
#ans0304 = np.dot(B, A)
#print('3.4) ', ans0304)
# [[-1, -5, -1]
#  [2, 7, 4]]


## 06.03.05
#ans0305 = np.dot(B, A.T)
#print('3.5) ', ans0305)
# not defined
#print('\n')


### 06.03 Optional

## 06.03.06
#ans0306 = np.dot(B, C)
#print('3.6) ', ans0306)
# not defined

## 06.03.07
#ans0307 = np.dot(C, B)
#print('3.7) ', ans0307)
# [[5, -6]
#  [9, -8]
#  [6, -6]]

## 06.03.08
#ans0308 = B^(4)
#print('3.8) ', ans0308)
# [[5, -5]
#  [4, 5]]

    
## 06.03.09
#ans0309 = np.dot(A, A.T)
#print('3.9) ', ans0309)
# [[14, 28]
#  [28, 69]]

## 06.03.10
#ans0310 = np.dot(D.T, D)
#print('3.10) ', ans0310)
# [[10, -4, 0]
#  [-4, 8, 8]
#  [0, 8, 10]]
