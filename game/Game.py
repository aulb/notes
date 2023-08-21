import random 

STARTING_NUM = 2

class Tile:
  def __init__(self, number=None):
    self.number = number
  
  def is_empty(self):
    return self.number is None
  
  def clear(self):
    self.number = None

  def double(self):
    self.number *= 2
  
  def __repr__(self):
    return str(self.number) if self.number is not None else 'x'
  
  def __eq__(self, other):
    return not self.is_empty() and not other.is_empty() and self.number == other.number
  
class Game:
  def __init__(self, size=4):
    self.size = size
    self._reset()

  def _reset(self):
    self.board = [[Tile() for _ in range(self.size)] for _ in range(self.size)]
    self.game_over = False
    self.num_of_moves = 0
    self.score = 0
    self.spawn_number()

  def spawn_number(self):
    empty_tiles = []
    for i in range(self.size):
      for j in range(self.size):
        curr_tile = self.board[i][j]
        if curr_tile.is_empty(): empty_tiles.append(curr_tile)
    if len(empty_tiles):
      empty_tiles[random.randrange(0, len(empty_tiles))].number = STARTING_NUM
    else:
      self.game_over = True

  def play(self):
    print(self)
    while not self.game_over:
      move = input('Move: ')
      if move not in ["L", "R", "U", "D"]:
        print("Wrong input")
      else:
        self.move(move)
    print("Game over")

  def move(self, key):
    # "L" and/or "R" is horizontal
    # "U" and/or "D" is vertical
    # Merge:
    # 1) "L" is left to right 1 "merge to the left"
    # 2) "R" is right to left -1 "merge to the right"
    # 3) "U" is up to down 1 "merge up"
    # 4) "D" is down to up -1 "merge down"
    # Shift:
    # 1) "L" is left shift, left to right 1
    # 2) "R" is right shift, right to left -1
    # 3) "U" is up down +1 
    # 4) "D" is down up -1
    if key in ("L", "R"):
      self.merge_horizontally(True if key == "L" else False)
      self.shift_horizontally(True if key == "L" else False)
    else:
      self.merge_vertically(True if key == "U" else False)
      self.shift_vertically(True if key == "U" else False)
    self.spawn_number()
    print(self)
  
  def _merge_helper(self, curr_tile, prev_tile):
    if not curr_tile.is_empty():
      if prev_tile == curr_tile:
        prev_tile.double()
        curr_tile.clear()
        return Tile()
      return curr_tile
    return prev_tile

  def merge_horizontally(self, left_to_right):
    for i in range(self.size):
      prev_tile = Tile()
      for j in (range(self.size) if left_to_right else range(self.size - 1, -1, -1)):
        prev_tile = self._merge_helper(self.board[i][j], prev_tile)

  def merge_vertically(self, top_to_bottom):
    for j in range(self.size):
      prev_tile = Tile()
      for i in (range(self.size) if top_to_bottom else range(self.size - 1, -1, -1)):
        prev_tile = self._merge_helper(self.board[i][j], prev_tile)

  def shift_horizontally(self, left_shift):
    for i in range(self.size):
      pj = None
      for j in (range(self.size) if left_shift else range(self.size - 1, -1, -1)):
        if pj is None: pj = j
        if not self.board[i][j].is_empty():
          self.board[i][j], self.board[i][pj] = self.board[i][pj], self.board[i][j]
          pj += (1 if left_shift else -1)

  def shift_vertically(self, top_shift):
    for j in range(self.size):
      pi = None
      for i in (range(self.size) if top_shift else range(self.size - 1, -1, -1)):
        if pi is None: pi = i
        if not self.board[i][j].is_empty():
          self.board[i][j], self.board[pi][j] = self.board[pi][j], self.board[i][j]
          pi += (1 if top_shift else -1)
        
  def __repr__(self):
    txt = ''
    for index, row in enumerate(self.board):
      txt += str(row) + ('\n' if index != self.size - 1 else '')
    return txt

if __name__ == "__main__":
  game = Game()
  game.play()
