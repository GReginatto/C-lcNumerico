def gauss_seidel(n, A, b, Toler, IterMax):
  Info = 1
  x = [b[i] / A[i][i] for i in range(0, n)]
  Iter = 0
  v = [0.0] * n

  while Iter < IterMax:
    Iter += 1
    NormaNum = 0
    NormaDen = 0
    
    for i in range(0, n):
      Soma = 0
      for j in range(0, n):
        if i != j:
          Soma = Soma + A[i][j] * x[j]
      
      v[i] = x[i]
      x[i] = (b[i] - Soma)/A[i][i]
      t = abs(x[i] - v[i])
      
      if t > NormaNum:
        NormaNum = t
      if abs(x[i]) > NormaDen:
        NormaDen = abs(x[i])
    
    NormaRel = NormaNum / NormaDen if NormaDen != 0 else 0
    print("Iter:", Iter, "x:", x, "NormaRel:", NormaRel)

    if NormaRel <= Toler or Iter >= IterMax:
      break

  if NormaRel <= Toler:
    Info = 0

  return x, Iter, Info
