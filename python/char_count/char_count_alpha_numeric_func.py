

def char_count_alpha_numeric(string):
    count = {}
    for char in string:
        if isAlphaNumeric(char):
            char = char.lower()
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
    return count

def isAlphaNumeric(char):
    code = ord(char)
    if (
        not (code > 47 and code < 58) and # match numeric (0-9)
        not (code > 64 and code < 91) and # match upper alpha (A-Z)
        not (code > 96 and code < 123)    # match lower alpha (a-z)
       ):
        return False
    return True

print(char_count_alpha_numeric("Hello! How are you? Call me at (212) 310-4153."))
