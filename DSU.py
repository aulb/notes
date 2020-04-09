class DSU:
  def __init__(self, size: int = 10) -> None:
    self.arr = list(range(size))

  def find(self, val: int) -> int:
    if self.arr[val] != val:
      self.arr[val] = self.find(self.arr[val])
    return self.arr[val]

  def union(self, child: int, parent: int) -> None:
    self.arr[self.find(child)] = self.find(parent)

dsu = DSU()
dsu.find(1)
dsu.union(2,3) # Make 2 the parent of 3
print(dsu.arr)
