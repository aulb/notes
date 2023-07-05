COOLDOWN = 5
cache = {}

def shouldPrintMessage(message, timestamp):
    latestTimestamp = cache.get(message, -1)
    if latestTimestamp == -1:
        cache[message] = timestamp
        return True
    canPrint = timestamp - latestTimestamp > COOLDOWN
    if canPrint:
        cache[message] = timestamp
    return canPrint

if __name__ == "__main__":
    testCases = [
        ['hi', 1],
        ['hi', 2],
        ['bye', 3],
        ['bye', 9],
        ['see', 10],
        ['bye', 12],
        ['see', 15],
        ['hi', 16],
    ]
    for testCase in testCases:
        print(testCase, shouldPrintMessage(*testCase))
    
    print(cache)
