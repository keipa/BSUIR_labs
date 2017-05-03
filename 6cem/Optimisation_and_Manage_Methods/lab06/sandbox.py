import  lab01sci
from numpy import *

m = 3
n = 8
B0 = array([[2, 1, 0, 4, 0, 3, 0, 0],
            [0, 4, 0, 3, 1, 1, 3, 2],
            [1, 3, 0, 5, 0, 4, 0, 4]])
B = array([[[0, 0, 0.5, 2.5, 1.0, 0, -2.5, -2.0],
            [0.5, 0.5, -0.5, 0, 0.5, -0.5, -0.5, -0.5],
            [0.5, 0.5, 0.5, 0, 0.5, 1.0, 2.5, 4.0]],
           [[1, 2, -1.5, 3, -2.5, 0, -1, -0.5],
            [-1.5, -0.5, -1, -2.5, 3.5, -3, -1.5, -0.5],
            [1.5, 2.5, -1, 1, 2.5, 1.5, 3, 0]],
           [[0.75, 0.5, -1, 0.25, 0.25, 0, 0.25, 0.75],
            [-1.0000, 1.0000, 4.0000, 0.7500, 0.7500, 0.5000, 7.0, -0.75],
            [0.5000, -0.2500, 0.5000, 0.75, 0.5000, 1.2500, -0.7500, -0.25]],
           [[1.5000, -1.5000, -1.5000, 2.0000, 1.5000, 0, 0.5000, -1.5000],
            [-0.5000, -2.5000, -0.5000, -5.0000, -2.5000, 3.5000, 1.0000, 2.0000],
            [-2.5000, 1.0000, -2.0000, -1.500, -2.5000, 0.5000, 8.5000, -2.5000]],
           [[1.0000, 0.2500, -0.5000, 1.2500, 1.2500, -0.5000, 0.2500, -0.7500],
            [-1.0000, -0.7500, -0.7500, 0.5000, -0.2500, 1.2500, 0.2500, -0.5000],
            [0, 0.7500, 0.5000, -0.5000, -1.0000, 1.0000, -1.0000, 1.0000]]])
c0 = array([-1, -1, -1, -1, -2, 0, -2, -3])
c = array([[0, 60, 80, 0, 0, 0, 40, 0],
           [2, 0, 3, 0, 2, 0, 3, 0],
           [0, 0, 80, 0, 0, 0, 0, 0],
           [0, -2, 1, 2, 0, 0, -2, 1],
           [-4, -2, 6, 0, 4, -2, 60, 2]])
alpha = array([-687.125, -666.625, -349.5938, -254.625, -45.1563])
x = array([0, 8, 2, 1, 0, 4, 0, 0])

lab01sci.convex(B0, c0, B, c, alpha, x)