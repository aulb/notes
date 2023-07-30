def breadthOfParentheses2(s):
  depthsBreadth = [0]
  maxBreadth = 0
  currDepth = 0
  for char in s:
    if char == "(":
      currDepth += 1
      if currDepth > len(depthsBreadth):
        depthsBreadth.append(0)
    else:
      print(depthsBreadth, currDepth)
      maxBreadth = max(maxBreadth, depthsBreadth[currDepth - 1])
      depthsBreadth[currDepth - 1] = 0
      currDepth -= 1
      if currDepth - 1 >= 0:
        depthsBreadth[currDepth - 1] += 1
  return maxBreadth

def breadthOfParentheses(s):
  depthsBreadth = {0: 0}
  maxBreadth = 0
  currDepth = 0
  for char in s:
    if char == "(":
      currDepth += 1
      depthsBreadth[currDepth] = 0
    else:
      maxBreadth = max(maxBreadth, depthsBreadth[currDepth])
      currDepth -= 1
      depthsBreadth[currDepth] += 1
  return maxBreadth

if __name__ == "__main__":
  testCases = [
    ["(()()())()", 3],
    ["()()()()", 0],
    ["(((((((()()()()()()()()()())())))()()()())))", 10]
  ]
  print(breadthOfParentheses(testCases[2][0]))