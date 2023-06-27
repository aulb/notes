from collections import Counter
def build_guess_result(answer, guess):
    answerCounter = Counter(answer)

    # SCARE, SCALE => "G,G,G,_,G"
    # APPLE, PAPER => "Y,Y,G,_,Y"
    # SAUCY, GLASS => "_,_,Y,Y,_" # This a tricky one to do it
    # STILT - Do a double pass
    result = []
    for index, char in enumerate(guess):
        if char in answerCounter:
            if char == answer[index]:
                result.append("G")
                # Used for cases like "GUEST" and "STILT"
                answerCounter[char] -= 1
            else:
                result.append("Y")
        else:
            result.append("_")
    
    # Validate
    for index, char in enumerate(guess):
        if result[index] == "Y":
            if answerCounter[char] == 0:
                result[index] = "+"
            else:
                answerCounter[char] -= 1

    return result

def get_max_char_limit(wordResult, word, charToCompare):
    maxLimit = 0
    for index, char in enumerate(word):
        if char == charToCompare and wordResult[index] in ["G", "Y"]: maxLimit += 1
    return maxLimit

def check_word(guessResult, guess, word):
    charNotIn = []
    charLimit = {}
    greens = [None] * 5
    yellows = [None] * 5

    for index, char in enumerate(guess):
        # Can't do this way because...
        if guessResult[index] == "_": 
            charNotIn.append(char)
        elif guessResult[index] == "G":
            greens[index] = char
        elif guessResult[index] == "Y":
            yellows[index] = char
        elif guessResult[index] == "+" and char not in charLimit:
             # count occurences of S
            charLimit[char] = get_max_char_limit(guessResult, guess, char)

    # ['G', 'L', 'A', 'S', 'S']
    # ['_', '_', 'Y', 'Y', '+'] ==> can't have more than 1 S
    wordCounter = Counter(word)
    for index, char in enumerate(word):
        if char in charNotIn: return False
        if greens[index] is not None and char != greens[index]: return False
        if yellows[index] is not None and char == yellows[index]: return False
        if char in charLimit and wordCounter[char] != charLimit[char]: return False
    return True


def guess_another_word(words, answer, guess):
    guessResult = build_guess_result(answer, guess)
    # ['G', 'G', 'G', '_', 'G'] SCARE - SCALE -> Find SCALE, SCAPE
    # ['_', '_', 'Y', 'Y', '_'] SAUCY - GLASS -> Find ASTRO for example
    # Words with S as their first letter, C as their second ... 
    # filter, words with L not in the 4th column, ... 
    # No P/L for example
    wordsFiltered = []
    for word in words:
        if word != guess and check_word(guessResult, guess, word): wordsFiltered.append(word)
    return wordsFiltered

# TODO...
def play():
    pass

if __name__ == "__main__":
    # ['Y', 'Y', '_', '_', '+'] WRONG
    # ['Y', '+', '_', '_', 'G'] CORRECT
    print(build_guess_result("GUEST", "STILT"))

    # ['G', 'G', 'G', '_', 'G']
    print(build_guess_result("SCARE", "SCALE"))
    # ['Y', 'Y', 'G', 'Y', '_']
    print(build_guess_result("APPLE", "PAPER"))
    # ['_', '_', 'Y', 'Y', '+']
    result1 = build_guess_result("SAUCY", "GLASS")
    print(result1)
    # print(get_max_char_limit(["_","+","Y","Y","+"], "GSASS", "S")) # 1

    words = ["SAUCY", "GLASS","ASTRO","SANDS"]
    print(guess_another_word(words, "SAUCY", "GLASS"))