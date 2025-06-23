def eliminacao_de_gausson(n, A, b):
    A = A.astype(float)
    b = b.astype(float)

    Det = 1
    Info = 0

    for j in range(0, n - 1):
        p = j
        Amax = abs(A[j][j])
        for k in range(j + 1, n):
            if abs(A[k][j]) > Amax:
                Amax = abs(A[k][j])
                p = k

        if p != j:
            for k in range(n):
                A[j][k], A[p][k] = A[p][k], A[j][k]
            b[j], b[p] = b[p], b[j]
            Det = -Det

        Det *= A[j][j]

        if abs(A[j][j]) != 0:
            r = 1 / A[j][j]
            for i in range(j + 1, n):
                Mult = A[i][j] * r
                A[i][j] = 0
                for k in range(j + 1, n):
                    A[i][k] -= Mult * A[j][k]
                b[i] -= Mult * b[j]
        else:
            if Info == 0:
                Info = j

    Det *= A[n - 1][n - 1]
    if Info == 0 and abs(A[n - 1][n - 1]) == 0:
        Info = n

    return A, b, Det, Info

