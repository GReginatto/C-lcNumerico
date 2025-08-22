import numpy as np
import math
import matplotlib.pyplot as plt

def rk(a, b, y0, m):
  h = (b - a)/m
  xt = a
  yt = y0
  VetX = [0] * (m + 1)
  VetY = [0] * (m + 1)
  VetX[0] = xt
  VetY[0] = yt

  for i in range (0, m):
    x = xt
    y = yt
    k1 = f(x, y)

    x = xt + h/2
    y = yt + (h/2)*k1
    k2 = f(x, y)

    y = yt + (h/2)*k2
    k3 = f(x, y)

    x = xt + h
    y = yt + h*k3
    k4 = f(x, y)

    xt = a + i * h
    yt = yt + (h/6)*(k1 + 2*k2 + 2*k3 + k4)

    VetX[i+1] = xt
    VetY[i+1] = yt

  return VetX, VetY


