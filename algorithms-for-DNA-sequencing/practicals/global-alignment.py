abt = ['A', 'C', 'G', 'T']
score = [[0, 4, 2, 4, 8],
         [4, 0, 4, 2, 8],
         [2, 4, 0, 4, 8],
         [4, 2, 4, 0, 8],
         [8, 8, 8, 8, 8]]

def globalAlignment(x, y):
  # Init
  D = []
  for i in range(len(x)+1):
    D.append([0] * (len(y)+1))
  for i in range(1, len(x)+1):
    D[i][0] = D[i-1][0] + score[abt.index(x[i-1])][-1]
  for i in range(1, len(y)+1):
    D[0][i] = D[0][i-1] + score[-1][abt.index(y[i-1])]

  for i in range(1, len(x)+1):
    for j in range(1, len(y)+1):
      delta = 0 if x[i-1] == y[j-1] else 1
      case1 = D[i-1][j-1] + score[abt.index(x[i-1])][abt.index(y[j-1])]
      case2 = D[i-1][j] + score[abt.index(x[i-1])][-1]
      case3 = D[i][j-1] + score[-1][abt.index(y[j-1])]
      D[i][j] = min(case1, case2, case3)

  return D[-1][-1]

x = 'TACCAGATTCGA'
y = 'TACCAGATTCGA'
print(globalAlignment(x, y))

x = 'TACCAGATTCGAA'
y = 'TACCAGATTCGA'

print(globalAlignment(x, y))

x = 'TACCAGATTCGAA'
y = 'TACCAGATTCGAG'

print(globalAlignment(x, y))