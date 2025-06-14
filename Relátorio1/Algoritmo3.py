import matplotlib.pyplot as plt
import numpy as np


def function(x):
    return x**3 - 5 * x**2 + x + 3

def derivative_function(x):
    return 3 * x**2 - 10 * x + 1

def derivative2_function(x):
    return 6 * x - 10


def newton_raphson(x0, precisionOne, precisionTwo):
    pontos = [(x0, function(x0))]
    segmentos = []
    k = 1

    while True:
        fx = function(x0)
        dfx = derivative_function(x0)
        x1 = x0 - fx / dfx

        print(f"Iteração {k}: x = {x1}")

        # ponto atual (x0, f(x0)), próximo ponto (x1, 0)
        segmentos.append(((x0, fx), (x1, 0)))
        pontos.append((x1, function(x1)))

        if abs(function(x1)) < precisionOne or abs(x1 - x0) < precisionTwo:
            break

        x0 = x1
        k += 1

    return x1, pontos, segmentos

x_vals = np.linspace(-4, 4, 400)
y_vals = function(x_vals)

plt.figure(figsize=(10, 7))
plt.plot(x_vals, y_vals, label='f(x) = x³ - 5x² + x + 3', color='blue')

px = [p[0] for p in pontos]
py = [p[1] for p in pontos]
plt.scatter(px, py, color='red', zorder=5, label='Iterações')

for p1, p2 in segmentos:
    plt.plot([p1[0], p2[0]], [p1[1], p2[1]], color='gray', linestyle='--')

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Método de Newton-Raphson')
plt.grid(True)
plt.legend()
plt.show()
