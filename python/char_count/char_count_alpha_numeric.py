

def char_count_alpha_numeric(string):
    count = {}
    for char in string:
        if char.isalpha() or char.isnumeric():
            char = char.lower()
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
    return count


print(char_count_alpha_numeric("Hello! How are you? Please call me at (212) 310-4153."))
