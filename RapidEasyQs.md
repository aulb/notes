- Intersection of Two Arrays
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) and set(nums2))

- Intersection of Two Arrays II
from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts = Counter(nums1)
        result = []
        for num in nums2:
            if num in counts and counts[num]:
                result.append(num)
                counts[num] -= 1
        return result

- Monotonic Array
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if len(A) < 3: return True
        prev = A[0]
        trend = None
        for i in range(1, len(A)):
            if A[i] == prev: continue
            if A[i] > prev and not trend: trend = 1
            if A[i] < prev and not trend: trend = -1

            if trend == 1 and A[i] < prev: return False
            if trend == -1 and A[i] > prev: return False
            prev = A[i]
        return True

- Closest BST Value (READ)
Not a simple left and right check. Need to check all closest
class Solution:
    def closestValue(root, target):
        closest = root.val
        if root.val < target:
            if root.right:
                right = closestValue(root.right, target)
                if abs(right - target) < abs(closest - target):
                    closest = right
        else:
            if root.left:
                left = closestValue(root.right, target)
                if abs(left - target) < abs(closest - target):
                    closest = left
        return closest

- Nested List Weight Sum
Use a helper.
def getDepthSum(nestedList, depth):
    return sum(
        item.getInteger() * depth if item.isInteger()
        else getDepthSum(item.getList(), depth + 1)
        for item in nestedList
    )
return getDepthSum(nestedList, 1)

- Island Perimeter
For each tile check top, left, right, down. If 0 or OOB, add to perimeter count.

- Third Maximum Number
Make sure you "set" it. Read instructions.
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums) # Trick
        if len(nums) < 3: return max(nums)
        maxNum = max(nums)
        secondMaxNum = -float("inf")
        for num in nums:
            if num > secondMaxNum and num < maxNum:
                secondMaxNum = num
        if secondMaxNum == -float("inf"): return maxNum
        thirdMaxNum = -float("inf")
        for num in nums:
            if num > thirdMaxNum and num < secondMaxNum:
                thirdMaxNum = num
        if thirdMaxNum == -float("inf"): return secondMaxNum
        return thirdMaxNum


- Average of Levels in Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        levels = []
        def dfs(node, level):
            if not node: return
            if len(levels) == level: levels.append([])
            levels[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        dfs(root, 0)
        return [sum(level)/len(level) for level in levels]

- Toeplitz Matrix
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        def checkDiagonal(i, j):
            prev = matrix[i][j]
            while 0 <= i < len(matrix) and 0 <= j < len(matrix[0]):
                if prev != matrix[i][j]: return False
                i += 1
                j += 1
            return True
        for i in range(len(matrix)):
            if not checkDiagonal(i, 0): return False
        for j in range(len(matrix[0])):
            if not checkDiagonal(0, j): return False
        return True

- Range Sum of BST
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.sumSoFar = 0
        def traverse(node):
            if not node: return
            if L <= node.val <= R: self.sumSoFar += node.val
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        return self.sumSoFar

- Symmetric Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isSym(left, right):
            if not left and not right: return True
            if not left or not right: return False
            return left.val == right.val and isSym(left.left, right.right) and isSym(left.right, right.left)
        return isSym(root, root)
