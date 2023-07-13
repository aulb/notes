def compress(string):
    if len(string) < 2: return string 
    return string[0] + str(len(string) - 2) + string[1]

def urlCompress(url):
    result = ""
    urlParts = filter(lambda x: len(x) > 2, url.split("/"))
    for urlPart in urlParts:
        parts = urlPart.split(".")
        for index, part in enumerate(parts):
            result += compress(part) + ("." if index != len(parts) - 1 else "")
        result += "/"
    return result

if __name__ == "__main__":
    # print(compress('alice'))
    print(urlCompress('https://www.serebii.net/pokedex-sv/fighting.shtml'))