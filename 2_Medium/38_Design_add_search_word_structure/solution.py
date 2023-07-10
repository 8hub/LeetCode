class WordDictionary:

    def __init__(self):
        self.trie = [{},False]

    def addWord(self, word: str) -> None:
        curr_trie_layer = self.trie
        for letter in word:
            if letter not in curr_trie_layer[0]:
                curr_trie_layer[0][letter] = [{},False]
            curr_trie_layer = curr_trie_layer[0][letter]
        curr_trie_layer[1] = True

    def search(self, word: str, curr_trie_layer = None) -> bool:
        if curr_trie_layer == None:
            curr_trie_layer = self.trie
        for idx, letter in enumerate(word):
            if letter == '.':
                return True in [self.search(word[idx+1:], curr_trie_layer[0][each_key]) for each_key in curr_trie_layer[0].keys()]
            if letter in curr_trie_layer[0].keys():
                curr_trie_layer = curr_trie_layer[0][letter]
            else:
                return False
        return curr_trie_layer[1]
            


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord('w')
obj.addWord('word')
obj.addWord('what')
obj.addWord('hard')
obj.addWord('woka')
obj.addWord('wops')
obj.addWord('world')
obj.addWord('hardly')
print(obj.search('word'))   #true
print(obj.search('what'))   #true
print(obj.search('wh'))     #false
print(obj.search('whathe')) #false
print(obj.search('rhat'))   #false
print(obj.search('wo.d'))   #true
print(obj.search('wo..'))   #true
print(obj.search('w..as'))   #false
print(obj.search('.'))   #false