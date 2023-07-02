letter_to_digit = {
  "a": 2, "b": 2, "c": 2,
  "d": 3, "e": 3, "f": 3,
  "g": 4, "h": 4, "i": 4,
  "j": 5, "k": 5, "l": 5,
  "m": 6, "n": 6, "o": 6,
  "p": 7, "q": 7, "r": 7, "s": 7, 
  "t": 8, "u": 8, "v": 8, 
  "w": 9, "x": 9, "y": 9, "z": 9,
}

def helperA(digits, word):
  if len(digits) == 0:
    return False, -1
  for index, letter in enumerate(word):
    if index < len(digits) and digits[index] != letter_to_digit[letter]:
      return False, -1
  return True, index

def solution(digits, words):    
  result = []
  for word in words:
    canBeMadeWithDigits, digitIndex = helperA(digits, word)
    if canBeMadeWithDigits:
      helper(result, [word], digits[digitIndex + 1:], words)
  return result

def helper(result, currentResult, digits, words):
  for word in words:
    canBeMadeWithDigits, digitIndex = helperA(digits, word)
    if canBeMadeWithDigits:
      copy = currentResult.copy()
      copy.extend([word])
      helper(result, copy, digits[digitIndex + 1:], words)
  result.append(currentResult)

  
if __name__ == "__main__":
  test1 = [2, 2, 8]
  words1 = ["act", "dap", "bat"]

  test2 = [7, 2, 4, 6, 2, 6, 9]
  words2 = ["rain", "bow", "rainbow", "pain", "any"]
  result2 = [
    ["rain", "bow"],
    ["rain", "any"],
    ["pain", "bow"],
    ["rain", "any"],
    ["rainbow"]
  ]

  print(solution(test2, words2))
  print(solution(test1, words1))