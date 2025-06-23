def eliminacao_de_gauss(A, b):
    n = len(b)
    A = A.astype(float)
    b = b.astype(float)

    for k in range(0, n - 1):
        for i in range(k + 1, n):
            m = A[i, k] / A[k, k]
            A[i, k] = 0
            for j in range(k + 1, n):
                A[i, j] = A[i, j] - m * A[k, j]
            b[i] = b[i] - m * b[k]

    x = np.zeros(n)
    x[n - 1] = b[n - 1] / A[n - 1, n - 1]

    for k in range(n - 2, -1, -1):
        s = 0
        for j in range(k + 1, n):
            s += A[k, j] * x[j]
        x[k] = (b[k] - s) / A[k, k]

    return x


