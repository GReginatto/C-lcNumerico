import numpy as np
import math
import matplotlib.pyplot as plt

# Segmento único

def trap(h,f0,f1):
  trap = h * (f0 + f1)/2
  return trap

# Múltiplos

def mTrap(h, n, f):
  sum = f[0]
  for i in range(1,n):
    sum = sum + 2 * f[i]
  sum = sum + f[n]
  mTrap = h * sum / 2
  return mTrap
