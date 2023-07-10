class Coordinate:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Size:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col

class Shape:
    def __init__(self, name: str, coordinate: Coordinate, size: Size):
        self.name = name
        self.coordinate = coordinate
        self.size = size

# 7:39
class Board:
    def __init__(self, boardLength: int, boardWidth: int):
        # Error check for valid length + width
        self.row = boardLength
        self.col = boardWidth
        self.shapes = {}
        self.shapeStack = []
        self._resetBoard()

    def _resetBoard(self):
        self.mat = [["0" for _ in range(self.col)] for _ in range(self.row)]
        
    def move(self, name: str, coordinate: Coordinate) -> None:
        if self.shapes.get(name, None) is None or \
            not self._validCoordinate(coordinate): return
        self.shapes[name].coordinate = coordinate

    def remove(self, name: str) -> None:
        if self.shapes.get(name, None) is None: return
        del self.shapes[name]
        for index, shape in enumerate(self.shapeStack):
            if shape.name == name: break
        self.shapeStack.pop(index)

    def draw(self, shape: Shape) -> None:
        if self.shapes.get(shape.name, None) is not None: return # 
        # Error check for valid coordinate
        self.shapes[shape.name] = shape
        self.shapeStack.append(shape)

    def _draw(self) -> None:
        for shape in self.shapeStack:
            coordinate = shape.coordinate
            size = shape.size
            # Draw from (2,2) size 2, 5
            for i in range(coordinate.x, coordinate.x + size.row):
                for j in range(coordinate.y, coordinate.y + size.col):
                    if not self._validCoordinate(Coordinate(i, j)): continue
                    self.mat[i][j] = shape.name
                
    def _validCoordinate(self, coordinate: Coordinate) -> bool:
        return coordinate.y < self.col and coordinate.y > 0 and coordinate.x > 0 and coordinate.x < self.row

    def __repr__(self) -> str:
        self._resetBoard()
        self._draw()
        board = ""
        for row in self.mat:
            board += str(row) + "\n"
        return board
    

if __name__ == "__main__":
    board = Board(10, 10)
    board.draw(Shape("c", Coordinate(3, 2), Size(2, 5)))
    print(board)
    board.draw(Shape("a", Coordinate(2, 2), Size(3, 3)))
    print(board)
    board.move("c", Coordinate(8, 1))
    print(board)
    board.remove("a")
    print(board)

