from typing import List, Optional
from dataclasses import dataclass

@dataclass
class IndexIndicator:
  isHorizontal: bool
  rowOrCol: int
  startIndex: int
  endIndex: int

  def __repr__(self):
    return f"{str(self.isHorizontal)} {str(self.isVertical)} {self.rowOrCol} {self.startIndex} {self.endIndex}"

def printRow(matrix) -> None:
  for row in matrix:
    print(row)

CONSECUTIVE_NUMBERS_LEN = 3
def zeroOutConsecutiveNumbers(matrix: List[List[int]]) -> None:
  if not matrix or not matrix[0]: return
  rowLen = len(matrix)
  colLen = len(matrix[0])
  indicesToZeroOut = []
  
  start, end = 0, 1
  prev = None
  for i in range(rowLen):
    for j in range(colLen + 1):
      # case special:
      if j == colLen:
        if end - start >= CONSECUTIVE_NUMBERS_LEN: 
          indicesToZeroOut.append(IndexIndicator(True, i, start, end))
        start, end = 0, 1
        prev = None
      # case 1 the same as prev
      elif prev == matrix[i][j]:
        end += 1
      # case 2 different from prev
      else:
        if end - start >= CONSECUTIVE_NUMBERS_LEN:
          indicesToZeroOut.append(IndexIndicator(True, i, start, end))
        prev = matrix[i][j]
        start, end = j, j + 1
  #############################################################################
  start, end = 0, 1
  prev = None
  for j in range(colLen):
    for i in range(rowLen + 1):
      # case special:
      if i == rowLen:
        if end - start >= CONSECUTIVE_NUMBERS_LEN: 
          indicesToZeroOut.append(IndexIndicator(False, j, start, end))
        start, end = 0, 1
        prev = None
      # case 1 the same as prev
      elif prev == matrix[i][j]:
        end += 1
      # case 2 different from prev
      else:
        if end - start >= CONSECUTIVE_NUMBERS_LEN:
          indicesToZeroOut.append(IndexIndicator(False, j, start, end))
        prev = matrix[i][j]
        start, end = i, i + 1
  #############################################################################
  for indexIndicator in indicesToZeroOut:
    if indexIndicator.isHorizontal:
      zeroOutHorizontal(matrix, indexIndicator.rowOrCol, indexIndicator.startIndex, indexIndicator.endIndex)
    else:
      zeroOutVertical(matrix, indexIndicator.rowOrCol, indexIndicator.startIndex, indexIndicator.endIndex)

def zeroOutHorizontal(matrix: List[List[int]], row: int, startIndex: int, endIndex: int):
  for j in range(startIndex, endIndex):
    matrix[row][j] = 0

def zeroOutVertical(matrix: List[List[int]], col: int, startIndex: int, endIndex: int):
  for i in range(startIndex, endIndex):
    matrix[i][col] = 0

if __name__ == "__main__":
  matrix1 = [
    [1,2,2,2,2],
    [1,2,2,2,2],
    [1,2,2,2,2],
    [2,2,2,2,8],
    [1,9,2,2,2],
  ]

  matrix1Expected = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,8],
    [0,0,0,0,0],
    [1,9,0,0,0],
  ]

  zeroOutConsecutiveNumbers(matrix1)
  printRow(matrix1)