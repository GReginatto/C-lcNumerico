import numpy as np
import math
import matplotlib.pyplot as plt

def lagrng(x,y,n, X):
  sum = 0

  for i in range (0, n):
    product = y[i]
    for j in range (0, n):
      if i != j:
        product = product * (X - x[j])/(x[i] - x[j])

    sum = sum + product

  lagrange = sum
  return lagrange

