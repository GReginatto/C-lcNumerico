import matplotlib.pyplot as plt
import numpy as np

def function (x):
  return x**3 - 9*x + 5

def bisection (a, b, precision):
  intermediate_roots = []
  if (function(a) * function(b) >= 0):
    return None, intermediate_roots
  if ((b-a) < precision):
    return (a+b)/2, intermediate_roots

  M = function(a)
  x = (a + b)/2
  intermediate_roots.append(x)

  while abs(function(x)) >= precision:

    print(f"Raiz intermediária: {x}")

    if ((M * function(x)) > 0):
      a = x
    else:
      b = x

    M = function(a)
    x = (a + b)/2
    intermediate_roots.append(x)

  return x, intermediate_roots



if bisection_points:
    x_pontos = bisection_points
    y_pontos = [function(x) for x in x_pontos]
else:
    x_pontos = []
    y_pontos = []


x_values = np.linspace(-4, 4, 200)
def function_alg1(x):
  return x**3 - 9*x + 5
y_values = function_alg1(x_values)

plt.figure(figsize=(10, 7))
plt.plot(x_values, y_values, label='f(x) = x^3 - 9x + 5')

if x_pontos:
    plt.scatter(x_pontos, y_pontos, color='red', zorder=5, label='Pontos da Bissecção')

plt.title('Gráfico da Função com Pontos da Bissecção')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
