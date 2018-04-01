i = None
res = None
S = None
N = None
m = None
matrix = None
j = None

def upRange(start, stop, step):
  while start <= stop:
    yield start
    start += abs(step)

def downRange(start, stop, step):
  while start >= stop:
    yield start
    start -= abs(step)

"""Find minimum coins required to make a change of
Rs N with m denomination coins stored in list S
"""
def findMinCoins(S, m, N):
  global i, res, matrix, j
  matrix = [float('inf')] * (N + 1)
  matrix[0] = 0
  for i in (1 <= float(N)) and upRange(1, float(N), 1) or downRange(1, float(N), 1):
    for j in S:
      if j <= i:
        res = matrix[int(((i + 1) - j) - 1)]
        if res != float('inf') and res + 1 < matrix[int((i + 1) - 1)]:
          matrix[int((i + 1) - 1)] = res + 1
  return matrix[int((N + 1) - 1)]

"""main
"""
def main():
  global i, res, S, N, m, matrix, j
  S = [1, 3, 5, 7]
  m = len(S)
  N = 18
  print(str('Minimum number of coins required to get desired change is ') + str(findMinCoins(S, m, N)))


main()