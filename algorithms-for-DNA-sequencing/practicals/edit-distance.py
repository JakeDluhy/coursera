def editDistRecursive(x, y):
    # This implementation is very slow
    if len(x) == 0:
        return len(y)
    elif len(y) == 0:
        return len(x)
    else:
        distHor = editDistRecursive(x[:-1], y) + 1
        distVer = editDistRecursive(x, y[:-1]) + 1
        if x[-1] == y[-1]:
            distDiag = editDistRecursive(x[:-1], y[:-1])
        else:
            distDiag = editDistRecursive(x[:-1], y[:-1]) + 1
        
        return min(distHor, distVer, distDiag)

def editDist(x, y):
  # Init
  D = []
  for i in range(len(x)+1):
    D.append([0] * (len(y)+1))
  for i in range(len(x)+1):
    D[i][0] = i
  for i in range(len(y)+1):
    D[0][i] = i

  for i in range(1, len(x)+1):
    for j in range(1, len(y)+1):
      delta = 0 if x[i-1] == y[j-1] else 1
      case1 = D[i-1][j-1] + delta
      case2 = D[i-1][j] + 1
      case3 = D[i][j-1] + 1
      D[i][j] = min(case1, case2, case3)

  return D[len(x)][len(y)]

s1 = 'shake spea'
s2 = 'Shakespear'
print(editDistRecursive(s1, s2))

print(editDist(s1, s2))