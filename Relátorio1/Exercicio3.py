e = 2.7  

def c(x):
    return 10 - 20 * (e**(-0.2 * x) - e**(-0.75 * x))

def dc(x):
    return 4 * (e ** (-0.2 * x)) - 15 * (e ** (-0.75 * x))

def f(x):
    return c(x) - 5

def df(x):
    return dc(x)

max_iter = 3
precision1 = 1e-2
precision2 = 1e-2
x0 = 1.0

def newton_raphson(x0, precisionOne, precisionTwo, max_iterations):
    pontos = [(x0, f(x0))]
    segmentos = []
    k = 1

    while True:
        fx = f(x0)
        dfx = df(x0)
        
        if dfx == 0:
            print("Derivada zero. Método falhou.")
            break
        
        x1 = x0 - fx / dfx
        
        print(f"Iteração {k}: x = {x1:.4f}, f(x) = {f(x1):.4f}")

        segmentos.append(((x0, fx), (x1, 0)))
        pontos.append((x1, f(x1)))

        if abs(f(x1)) < precisionOne or abs(x1 - x0) < precisionTwo or k >= max_iterations:
            break

        x0 = x1
        k += 1

    return x1, pontos, segmentos

raiz, pontos, segmentos = newton_raphson(x0, precision1, precision2, max_iter)

print(f"\nRaiz aproximada: x = {raiz:.4f}, c(x) = {c(raiz):.4f}")
