def fatoracao_cholesky(n, A):
  A = A.astype(float)
  Det = 1
  Info = 0

  for j in range(0, n):
    s = 0
    for k in range(j):
      s = s + (A[j][k] ** 2)

    t = A[j][j] - s

    if abs(t) > 0:
      A[j][j] = math.sqrt(t)
      r = 1.0 / A[j][j]
      Det = Det * t
    else:
      Info = j
      print("Matriz não é definida positiva")
      return None, None, Info
    for i in range(j + 1, n):
      s = 0
      for k in range(0, j):
        s = s + (A[i][k] * A[j][k])
      A[i][j] = (A[i][j] - s) * r

  return A, Det, Info

