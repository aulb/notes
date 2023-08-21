board = [
  [0,2,2,4],
  # [0,0,2,4],
  # [0,0,2,4],
  # [0,0,2,4],
]

board2 = [
  [16, 4, 4, 0],
]

# def _merge_helper(self, curr_tile, prev_tile):
#   if not curr_tile.is_empty():
#     if prev_tile == curr_tile:
#       prev_tile.double()
#       curr_tile.clear()
#       return Tile()
#     return curr_tile
#   return prev_tile

# def merge_horizontally(self, left_to_right):
#   for i in range(self.size):
#     prev_tile = Tile()
#     for j in (range(self.size) if left_to_right else range(self.size - 1, -1, -1)):
#       prev_tile = self._merge_helper(self.board[i][j], prev_tile)

def shift_horizontally(left_shift, size=4):
  for i in range(1):
    pj = None
    for j in (range(4) if left_shift else range(4 - 1, -1, -1)):
      if pj is None: pj = j
      if not board[i][j] == 0:
        print((i, j), (i, pj), board[i][j])
        board[i][j], board[i][pj] = board[i][pj], board[i][j]
        pj = pj + (1 if left_shift else -1)

if __name__ == "__main__":
  shift_horizontally(board)
  for row in board:
    print(row)
