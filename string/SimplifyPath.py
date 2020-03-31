class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = []
        for dirName in path.split("/"):
            if dirName == "..": paths.pop() if len(paths) else None
            elif dirName == ".": pass
            elif dirName != "": paths.append(dirName)
        return "/" + "/".join(paths)
        # paths = []
        # prevDir = ".."
        # currDir = "."
        # dirName = ""
        # for s in path + "/":
        #     if s == "/":
        #         if dirName == "": continue
        #         else:
        #             if dirName == prevDir:
        #                 if len(paths): paths.pop()
        #             elif dirName == currDir:
        #                 pass
        #             else:
        #                 paths.append(dirName)
        #         dirName = ""
        #         continue
        #     dirName = dirName + s
        # return "/" + "/".join(paths)
