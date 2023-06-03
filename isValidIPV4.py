import re

leading3To9 = r'[3-9][0-9]?$'
upTo255 = r'2[0-5]?[0-9]?$' 

def isValid(ipv4):
    strs = ipv4.split(".")
    for string in strs:
        if string.startswith("0") and len(string) == 1: continue
        if string.startswith("1"): continue
        if re.match(upTo255, string) is not None: continue
        if re.match(leading3To9, string) is not None: continue
        return False
    return True

if __name__ == "__main__":
    print(isValid("0.9.255.51") == True)
    print(isValid("0.9.300.51") == False)
    print(isValid("02.9.2.51") == False)
    print(isValid("02.9.2.510") == False)
    print(isValid("255.255.255.255") == True)
    print(isValid("1.2.3.40") == True)
    print(isValid("20.20.29.29") == True)