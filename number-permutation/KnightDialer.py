import math
# def generateDistMatrix(start):
#   lookup = [[0,0,0,0] for i in range(4)]
#   row, col = start
#   for i in range(4):
#     for j in range(4):
#       lookup[i][j] = manhattanDist(start, (i, j))
#   return lookup

# def printMatrix(matrix):
#   for row in matrix:
#     print(row)

def manhattanDist(start, dest):
  a = start[0] - dest[0]
  b = start[1] - dest[1]
  return max(abs(a), abs(b))

def getLocation(needle, haystack, squareSize):
  idx = haystack.index(needle)
  row = idx // squareSize
  col = idx % squareSize
  return (row, col)

def getTotalTime(password, keypad):
  if not password: return 0
  totalTime = 0
  prev = password[0]
  for i in range(1, len(password)):
    char = password[i]
    start = getLocation(prev, keypad, 4)
    dest = getLocation(char, keypad, 4)
    totalTime += manhattanDist(start, dest)
  return totalTime
