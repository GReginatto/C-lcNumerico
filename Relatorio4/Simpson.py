import numpy as np
import math
import matplotlib.pyplot as plt

# único

def sim13(h, f0, f1, f2):
  sim13 = 2 * h * (f0 + 4 * f1 + f2)/6
  return sim13

def sim38(h, f0, f1, f2, f3):
  sim38 = 3 * h * (f0 + 3 * f1 + 3 * f2 + f3)/8
  return sim38

# múltiplo

def mSim13(h, n, f):
  sum = f[0]
  for i in range(1,n-1,2):
    sum = sum + 4 * f[i] + 2 * f[i+1]

  sum = sum + 4 * f[n-1] + f[n]
  mSim13 = h * sum / 3
  return mSim13

def simpInt(a, b, n, f):
  h = (b - a) / n
  if n == 1:
    sum = trap(h, f[0], f[1])
  else:
    m = n
    odd = n/2 - int(n /2)
    if (odd > 0 and n > 1):
      sum = sum + sim38(h, f[0], f[1], f[2], f[3])
      m = n - 3
    if (m > 1):
      sum = sum + mSim13(h, m, f)

  simpInt = sum
  return simpInt
