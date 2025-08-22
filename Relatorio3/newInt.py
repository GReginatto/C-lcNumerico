import numpy as np
import math
import matplotlib.pyplot as plt

def newtInt(x, y, n, xi, yint, ea):
  fdd = np.zeros((n,n))

  for i in range (0, n):
    fdd[i][0] = y[i]

  for j in range (1, n):
    for i in range (0,n - j):
      fdd[i][j] = (fdd[i+1][j-1] - fdd[i][j-1])/(x[i+j] - x[i])

  xterm = 1
  yint[0] = fdd[0][0]

  for order in range (1, n):
    xterm = xterm * (xi - x[order - 1])
    yint2 = yint[order - 1] + fdd[0][order] * xterm
    ea[order - 1] = yint2 - yint[order - 1]
    yint[order] = yint2

