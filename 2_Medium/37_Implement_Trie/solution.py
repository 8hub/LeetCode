

class Trie:
    #dictionaries with key:char value:[{next_dict}, isWordEnd:bool]

    def __init__(self):
        self.trie = [{}, False]

    def insert(self, word: str) -> None:
        current_layer = self.trie
        idx = 0
        length = len(word)
        for idx in range(length):
            if word[idx] not in current_layer[0].keys():
                current_layer[0][word[idx]] = [{}, False]
            current_layer = current_layer[0][word[idx]]
            if idx == length-1:
                current_layer[1] = True
        current_layer[0]
                
    def search(self, word: str) -> bool:
        current_layer = self.trie
        for char in word:
            if char in current_layer[0]:
                current_layer = current_layer[0][char]
            else:
                return False
        return current_layer[1]

    def startsWith(self, prefix: str) -> bool:
        current_layer = self.trie
        for char in prefix:
            if char in current_layer[0]:
                current_layer = current_layer[0][char]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("siema")
print(obj.search("siema"))
print(obj.search("siemaa"))
print(obj.startsWith("siemaa"))
print(obj.startsWith("siema"))
print(obj.startsWith("sia"))