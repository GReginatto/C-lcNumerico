import matplotlib.pyplot as plt
import numpy as np


def function(x):
  return 2 * x**3 + 5 * x**2 - 8 * x - 10

def false_position(a, b, precision1, precision2):
    pontos_intermediarios = []
    segmentos = []

    if function(a) * function(b) >= 0:
        return None, pontos_intermediarios, segmentos

    k = 1
    while True:
        fa = function(a)
        fb = function(b)
        x = (a * fb - b * fa) / (fb - fa)
        fx = function(x)

        pontos_intermediarios.append(x)
        segmentos.append(((a, fa), (b, fb)))

        if abs(fx) < precision2 or (b - a) < precision1:
            return x, pontos_intermediarios, segmentos

        if fa * fx > 0:
            a = x
        else:
            b = x
        if (b - a) < precision1:
            return (a + b) / 2, pontos_intermediarios

        k += 1

x_vals = np.linspace(-4, 4, 400)
y_vals = function(x_vals)

plt.figure(figsize=(10, 7))
plt.plot(x_vals, y_vals, label='f(x) = 2x³ + 5x² -8x +10')

y_pontos = [function(x) for x in pontos]
plt.scatter(pontos, y_pontos, color='red', label='Pontos da Falsa Posição', zorder=5)

for (p1, p2) in segmentos:
    plt.plot([p1[0], p2[0]], [p1[1], p2[1]], color='gray', linestyle='--', alpha=0.7)

plt.title('Método da Falsa Posição com Retas Secantes')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.show()
