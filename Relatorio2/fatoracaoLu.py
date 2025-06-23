def fatoracao_LU(m, n , A):
  A = A.astype(float)
  Pivot = list(range(m))
  PdU = 1.0
  Info = 0

  for j in range(min(m, n)):
    p = j
    Amax = abs(A[j][j])
    for k in range(j + 1, m):
      if abs(A[k][j]) > Amax:
        Amax = abs(A[k][j])
        p = k
    if p != j:
        A[[j, p], :] = A[[p, j], :]
        Pivot[j], Pivot[p] = Pivot[p], Pivot[j]
        PdU = -PdU

        PdU *= A[j][j]

        if abs(A[j][j]) != 0:
            r = 1.0 / A[j][j]
            for i in range(j + 1, m):
                Mult = A[i][j] * r
                A[i][j] = Mult
                for k in range(j + 1, n):
                    A[i][k] = A[i][k] - Mult * A[j][k]
        else:
            if Info == 0:
                Info = j

    return A, Pivot, PdU, Info
