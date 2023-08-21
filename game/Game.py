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
  
  def __eq__(self, other_tile):
    return other_tile.number == self.number and not other_tile.is_empty() and not self.is_empty()

class Game:
  def __init__(self):
    self._reset()

  def _reset(self):
    self.board = [[Tile() for _ in range(4)] for _ in range(4)]
    self.game_over = False
    self.num_of_moves = 0
    self.score = 0
    # self.spawn_number()

  def spawn_number(self):
    empty_tiles = []
    for i in range(4):
      for j in range(4):
        curr_tile = self.board[i][j]
        if curr_tile.is_empty(): empty_tiles.append(curr_tile)
    if len(empty_tiles):
      empty_tiles[random.randrange(0, len(empty_tiles))].number = STARTING_NUM
    else:
      self.game_over = True

  def play(self):
    while not self.game_over:
      guess = int(input('Move'))
      if guess not in ["l", "r", "u", "d"]: 
        print("Wrong input")
      else:
        self.move(guess)
      print(self)
      self.spawn_number()

  def move(self, key):
    if key == "l" or key == "r":
      update = "ROW"
      direction = 1 if key == "l" else -1 
    else:
      update = "COL"
      direction = 1 if key == "u" else -1
    self._update(update, direction)

  def _update(self, update, direction):
    if update == "ROW":
      self._merge_horizontal(direction == -1)
      self._shift_horizontal(direction == -1)
    else:
      self._merge_vertical(direction == -1)
      self._shift_vertical(direction == -1)

  def _merge_horizontal(self, backward):
    cols = list(range(4))
    if backward: cols.reverse()
    prev_tile = Tile()
    for i in range(4):
      for j in cols:
        curr_tile = self.board[i][j]
        if curr_tile == prev_tile:
          prev_tile.double()
          curr_tile.clear()
        prev_tile = curr_tile

  def _merge_vertical(self, backward):
    rows = list(range(4))
    if backward: rows.reverse()
    prev_tile = Tile()
    for j in range(4):
      for i in rows:
        curr_tile = self.board[i][j]
        if curr_tile == prev_tile:
          prev_tile.double()
          curr_tile.clear()
        prev_tile = curr_tile

  def _shift_horizontal(self, backward):
    cols = list(range(4))
    if backward: cols.reverse()
    prev_tile = Tile()
    for i in range(4):
      for j in cols:
        curr_tile = self.board[i][j]
        if curr_tile == prev_tile:
          prev_tile.double()
          curr_tile.clear()
        prev_tile = curr_tile

  def _shift_vertical(self, backward):
    rows = list(range(4))
    if backward: rows.reverse()
    prev_tile = Tile()
    for j in range(4):
      for i in rows:
        curr_tile = self.board[i][j]
        if curr_tile == prev_tile:
          prev_tile.double()
          curr_tile.clear()
        prev_tile = curr_tile

  def __repr__(self):
    txt = ''
    for index, row in enumerate(self.board):
      txt = txt + str(row) + ('\n' if index != 3 else '')
    return txt

if __name__ == "__main__":
  game = Game()
  game._merge_vertical(True)
  print(game)
