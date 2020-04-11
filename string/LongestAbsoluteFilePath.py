class Solution:
    def lengthLongestPath(self, input: str) -> int:
        input = input.split('\n')
        if not input: return 0

        def isFile(s: str):
            return s.find('.') != -1

        def countDepth(s: str):
            return s.count('\t')

        maxLength = 0
        stack = []
        for item in input:
            if isFile(item):
                dirName = '/'.join(stack)
                if dirName != '': dirName += '/'
                maxLength = max(maxLength, len(dirName + item.replace('\t', '')))
                continue

            depth = countDepth(item)
            while len(stack) > depth:
                stack.pop()
            stack.append(item.replace('\t', ''))


        return maxLength
