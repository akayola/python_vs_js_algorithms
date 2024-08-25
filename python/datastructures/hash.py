def hash(key, arrayLen):
    total = 0
    prime = 31
    for i in range(min(len(key), 100)):
        char = key[i]
        value = ord(char) - 96
        total = (total * prime + value) % arrayLen
    return total

print(hash('orange', 13))
print(hash('hello', 13))
print(hash('blue', 13))
print(hash('green', 13))
