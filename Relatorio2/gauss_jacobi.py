def gauss_jacobi(n, A, b, Toler, IterMax):
    x = [b[i] / A[i][i] for i in range(0, n)] 
    v = [0.0] * n
    Iter = 0
    info = 1  

    while Iter < IterMax:
        Iter += 1

        for i in range(n):
            Soma = 0
            for j in range(n):
                if j != i:
                    Soma += A[i][j] * x[j]
            v[i] = (b[i] - Soma) / A[i][i]

        NormaNum = 0
        NormaDen = 0

        for i in range(n):
            t = abs(v[i] - x[i])
            if t > NormaNum:
                NormaNum = t
            if abs(v[i]) > NormaDen:
                NormaDen = abs(v[i])

        for i in range(n):
            x[i] = v[i] 

        NormaRel = NormaNum / NormaDen if NormaDen != 0 else 0

        print("Iter:", Iter, "x:", x, "NormaRel:", NormaRel)

        if NormaRel <= Toler:
            info = 0  
            break

    return x, Iter, info


