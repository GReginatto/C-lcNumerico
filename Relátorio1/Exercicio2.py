import numpy as np
import matplotlib.pyplot as plt

def f(h):
    return (np.pi * h**2 / 3) * (3 - h) - 0.5

def df(h):
    return (np.pi / 3) * (6*h - 3*h**2)

precision1 = 1e-2
precision2 = 1e-2
max_iter = 3

# Bissecção
def bisseccao(a, b):
    pontos = []
    if f(a) * f(b) >= 0:
        return None, pontos
    for _ in range(max_iter):
        c = (a + b) / 2
        pontos.append(c)
        if abs(f(c)) < precision2 or abs(b - a) < precision1:
            break
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c, pontos

# Falsa posição
def falsa_posicao(a, b):
    pontos = []
    if f(a) * f(b) >= 0:
        return None, pontos
    for _ in range(max_iter):
        fa, fb = f(a), f(b)
        c = (a * fb - b * fa) / (fb - fa)
        pontos.append(c)
        if abs(f(c)) < precision2 or abs(b - a) < precision1:
            break
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c, pontos

# Secante
def secante(a, b):
    pontos = [a, b]
    for _ in range(max_iter):
        fa, fb = f(a), f(b)
        if fb - fa == 0:
            return None, pontos
        c = b - fb * (b - a) / (fb - fa)
        pontos.append(c)
        if abs(f(c)) < precision2 or abs(c - b) < precision1:
            break
        a, b = b, c
    return c, pontos

# A
a1, b1 = 0.25, 0.5
biss_a, it_biss_a = bisseccao(a1, b1)
fp_a, it_fp_a = falsa_posicao(a1, b1)
sec_a, it_sec_a = secante(a1, b1)

print("\n--- Parte A ---")
if biss_a is None:
    print("Bissecção: Falhou | Iterações:", it_biss_a)
else:
    print(f"Bissecção: {biss_a:.6f} | Iterações: {it_biss_a}")

if fp_a is None:
    print("Falsa Posição: Falhou | Iterações:", it_fp_a)
else:
    print(f"Falsa Posição: {fp_a:.6f} | Iterações: {it_fp_a}")

print(f"Secante: {sec_a:.6f} | Iterações: {it_sec_a}")

# B
a2, b2 = 2.5, 3
biss_b, it_biss_b = bisseccao(a2, b2)
fp_b, it_fp_b = falsa_posicao(a2, b2)
sec_b, it_sec_b = secante(a2, b2)

print("\n--- Parte B ---")
if biss_b is None:
    print("Bissecção: None | Iterações:", it_biss_b)
else:
    print(f"Bissecção: {biss_b:.6f} | Iterações: {it_biss_b}")

if fp_b is None:
    print("Falsa Posição: None | Iterações:", it_fp_b)
else:
    print(f"Falsa Posição: {fp_b:.6f} | Iterações: {it_fp_b}")

print(f"Secante: {sec_b:.6f} | Iterações: {it_sec_b}")
