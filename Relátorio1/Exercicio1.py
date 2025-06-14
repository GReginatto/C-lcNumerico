import numpy as np
import matplotlib.pyplot as plt

def function(x):
    return 2.02 * x**5 - 1.28 * x**4 + 3.06 * x**3 - 2.92 * x**2 - 5.66 * x + 6.08

a, b = -2.0, 0.0
max_iter = 3
precision1 = 1e-2
precision2 = 1e-2

# Método da Bissecção
def bisection(a, b, precision1):
    intermediate_roots = []
    if function(a) * function(b) >= 0:
        return None, intermediate_roots

    x = (a + b) / 2
    intermediate_roots.append(x)
    k = 1

    while abs(function(x)) >= precision1 and k < max_iter:
        if function(a) * function(x) > 0:
            a = x
        else:
            b = x
        x = (a + b) / 2
        intermediate_roots.append(x)
        k += 1

    return x, intermediate_roots

# Método da Falsa Posição
def false_position(a, b, precision1, precision2):
    points = []
    if function(a) * function(b) >= 0:
        return None, points

    k = 1
    while k <= max_iter:
        fa = function(a)
        fb = function(b)
        x = (a * fb - b * fa) / (fb - fa)
        fx = function(x)
        points.append(x)

        if abs(fx) < precision2 or abs(b - a) < precision1:
            return x, points

        if fa * fx > 0:
            a = x
        else:
            b = x
        k += 1

    return x, points

# Método da Secante
def secant(a, b, precision1, precision2):
    points = [(a, function(a)), (b, function(b))]
    k = 1

    while k <= max_iter:
        fa = function(a)
        fb = function(b)
        if fb - fa == 0:
            return None, points

        x2 = b - fb * (b - a) / (fb - fa)
        fx2 = function(x2)
        points.append((x2, fx2))

        if abs(fx2) < precision2 or abs(x2 - b) < precision1:
            return x2, points

        a, b = b, x2
        k += 1

    return x2, points

bissec_result, bissec_points = bisection(a, b, precision1)
falsa_result, falsa_points = false_position(a, b, precision1, precision2)
secante_result, secante_points = secant(a, b, precision1, precision2)

x_vals = np.linspace(-2, 0, 400)
y_vals = function(x_vals)

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label="f(x)", color="black")
plt.axhline(0, color='gray', linewidth=0.8, linestyle='--')
plt.axvline(0, color='gray', linewidth=0.8, linestyle='--')

plt.scatter(bissec_points, [function(x) for x in bissec_points], color='red', label="Bissecção", zorder=5)
plt.scatter(falsa_points, [function(x) for x in falsa_points], color='blue', label="Falsa Posição", zorder=5)
plt.scatter([x for x, _ in secante_points], [function(x) for x, _ in secante_points], color='deeppink', label="Secante", zorder=5)

plt.title("Comparação dos Métodos - Raiz de f(x) no intervalo [-2, 0]")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

print("Resultado Bissecção:", round(bissec_result, 4))
print("Iterações Bissecção:", bissec_points)

print("Resultado Falsa Posição:", round(falsa_result, 4))
print("Iterações Falsa Posição:", falsa_points)

print("Resultado Secante:", round(secante_result, 4))
print("Iterações Secante:", [round(x, 4) for x, _ in secante_points])
