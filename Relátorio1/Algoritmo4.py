import matplotlib.pyplot as plt
import numpy as np

def function(x):
  return x**2 + x - 6

def secant(x0, x1, precisionOne, precisionTwo):
  if (abs(function(x0)) == 0):
    return None

  points = [(x0, function(x0)), (x1, function(x1))]

  if (abs(function(x0)) < precisionOne):
    return x0

  if (abs(function(x1)) < precisionOne):
    return x1

  if (abs(x1 - x0) < precisionTwo):
    return x1

  k = 1


  while True:
    x2 = x1 - (function(x1)/ (function(x1) - function(x0))) * (x1 - x0)
    points.append((x2, function(x2)))



    print(f"Iteração {k}: x = {x2}")

    if (abs(function(x2)) < precisionTwo):
      return x2,  points

    x0 = x1
    x1 = x2

    k = k + 1

# Dados para o gráfico
x_vals = np.linspace(-4, 4, 400)
y_vals = function(x_vals)

# Gráfico
plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label='f(x) = x² + x - 6', color='blue')

# Iterações e secantes
for i in range(1, len(iter_points)):
    x_prev, y_prev = iter_points[i - 1]
    x_curr, y_curr = iter_points[i]
    plt.plot([x_prev, x_curr], [y_prev, y_curr], 'k--', alpha=0.6)  # secante
    plt.plot(x_curr, y_curr, 'ro')  # ponto

# Estética
plt.title("Método da Secante")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.8)
plt.legend()
plt.show()
