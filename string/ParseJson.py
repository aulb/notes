def parse_json(string):
    string = string[1:-1]
    result = {}
    currentKey = None
    currentVal = None
    buildingKey = False
    keyBuilt = False
    isString = False
    for char in string:
        if char == "\"":
            if keyBuilt is False:
                if buildingKey is False:
                    buildingKey = True
                else:
                    keyBuilt = True
                    buildingKey = False
            else:
                isString = True
        else:
            if char == ",":
                if buildingKey:
                    currentKey += char
            if buildingKey:
                currentKey += char
            else:
                currentVal += char

      

if __name__ == "__main__":
    test1 = '{"hello": true, "world": false}'
    test2 = '{}'