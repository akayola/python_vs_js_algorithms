# hash_table.py

class HashTable:
    def __init__(self, size=53):
        self.keyMap = [None] * size

    def __repr__(self):
        return f'{type(self).__name__}({self.keyMap!r}, {self.size!r})'

    def _hash(self, key):
        total = 0
        prime = 31
        for i in range(min(len(key), 100)):
            char1 = key[i]
            value = ord(char1) - 96
            total = (total * prime + value) % len(self.keyMap)
        return total

    def set(self, key, value):
        index = self._hash(key)
        if not self.keyMap[index]:
            self.keyMap[index] = []
        self.keyMap[index].append([key, value])

    def get(self, key):
        index = self._hash(key)
        if self.keyMap[index]:
            for i in range(len(self.keyMap[index])):
                if self.keyMap[index][i][0] == key:
                    return self.keyMap[index][i][1]
        return None

    def keys(self):
        keysArr = []
        for i in range(len(self.keyMap)):
            if self.keyMap[i]:
                for j in range(len(self.keyMap[i])):
                    #if not keysArr.index(self.keyMap[i][j][1]):
                    #print(self.keyMap[i][j][1])
                    keysArr.append(self.keyMap[i][j][0])
        return keysArr

    def values(self):
        valuesArr = []
        for i in range(len(self.keyMap)):
            if self.keyMap[i]:
                for j in range(len(self.keyMap[i])):
                    #if not valuesArr.index(self.keyMap[i][j][1]):
                    valuesArr.append(self.keyMap[i][j][1])
        return valuesArr


ht = HashTable(17)

ht.set("maroon","#800000")
ht.set("yellow","#FFFF00")
ht.set("olive","#808000")
ht.set("salmon","#FA8072")
ht.set("lightcoral","#F08080")
ht.set("mediumvioletred","#C71585")
ht.set("plum","#DDA0DD")
ht.set("plum","Mumu")

print(ht.get("plum"))
print(ht.get("yellow"))
print(ht.get("hello"))

print(ht.keys())
print(ht.values())
