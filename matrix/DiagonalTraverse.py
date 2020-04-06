class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        ## THE MOST IMPORTANT OBSERVATION IS THAT i + j is always the same for diagonal
        if not matrix or not len(matrix) or not matrix[0]: return []
        result = []
        dd = collections.defaultdict(list)
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                dd[i+j].append(matrix[i][j])
        for k in dd.keys():
            if not k%2: dd[k].reverse()
            result += dd[k]
        return result
