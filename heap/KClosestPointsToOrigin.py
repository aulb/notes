import math
import heapq
class Node:
    def __init__(self, point, distance):
        self.point = point
        self.distance = distance

    def __lt__(self, other):
        return self.distance > other.distance

    def __repr__(self):
        return str(self.point) + ' - ' + str(self.distance)


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        nodes = []
        for point in points:
            heapq.heappush(nodes, Node(point, self.distFromOrigin(point)))
            if len(nodes) > K:
                heapq.heappop(nodes)
        return [node.point for node in nodes]

    def distFromOrigin(self, point):
        return math.sqrt(point[0] ** 2 + point[1] ** 2)

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for (x, y) in points:
            distance = -(x*x + y*y)
            if len(heap) == k:
                heapq.heappushpop(heap, (distance, x, y))
            else:
                heapq.heappush(heap, (distance, x, y))
        return [[x, y] for (distance, x, y) in heap]