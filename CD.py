def cd(currentPath, newPath):
    currentPaths = currentPath.split("/")
    if newPath.startswith("/"):
        currentPaths = []
    currentPaths = list(filter(lambda x: x != "", currentPaths))
    newPaths = newPath.split("/")
    for path in newPaths:
        if path == "..":
            if currentPaths: currentPaths.pop()
        elif path != "." and path != "":
            currentPaths.append(path)
    return "/" + "/".join(currentPaths)

def cdToSimplify(currentPath, newPath):
    currentPaths = currentPath.split("/")
    if newPath.startsWith("/"):
        currentPaths = []
    currentPaths = filter(lambda x: x != "", currentPaths)
    newPaths = newPath.split("/")
    for path in newPaths:
        if path == "": continue
        if path == "..":
            if currentPaths: currentPaths.pop()
        elif path == ".":
            pass
        else:
            currentPaths.append(path)
    return "/" + "/".join(currentPaths)

if __name__ == "__main__":
    testCases = [
        ["/", "a"],
        ["/", "."],
    ]

    for case in testCases:
        print(cd(*case))