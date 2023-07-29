from typing import List

def sumAroundRadius(matrix: List[int], radius: int) -> List[int]:
  if not matrix or not matrix[0]: return []
  m = len(matrix) # row
  n = len(matrix[0]) # col
  result = [[0 for j in range(n)] for i in range(m)]

  for i in range(m):
    for j in range(n):
      result[i][j] = getSumAroundCoordinate(matrix, m, n, radius, i, j)
  return result

def getSumAroundCoordinate(matrix: List[int], m: int, n: int, radius: int, i: int, j: int) -> int:
  total = 0
  for x in range(i - radius, i + radius + 1):
    for y in range(j - radius, j + radius + 1):
      if isValidCoordinate(m, n, x, y):
        total += matrix[x][y]
  return total

def isValidCoordinate(m: int, n: int, x:int, y: int) -> bool:
  return x >= 0 and y >= 0 and x < m and y < n

def printRow(matrix: List[int]) -> None:
  for row in matrix: print(row)


def range_sum2(matrix, r):
  def getsum(A, m, n, x, y, r):
      sums, start, end = 0, 0, 0
      for i in range(max(0, x-r), min(m, x+r+1)):
        if y > r:
            start = A[i][max(0, y-r-1)]
        end = A[i][min(n-1, y+r)]
        sums += end - start
      return sums

  m = len(matrix)
  n = len(matrix[0])
  res = [[0] * n for _ in range(m)]
  B = [row[:]for row in matrix]

  for i in range(m):
      for j in range(1,n):
        B[i][j] += B[i][j-1]
  for i in range(m):
      for j in range(n):
        res[i][j] = getsum(B, m, n, i, j, r)
  return res
	  

if __name__ == "__main__":
  test = [
    [1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,1,1,1],
  ]

  printRow(sumAroundRadius(test, 2)) # 15mins
  printRow(range_sum2(test, 2))

