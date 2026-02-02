class Node:
    def __init__(self, char=None, children=None, end_of_word=False):
        self.char = char
        self.children = [None] * 26
        self.end_of_word = end_of_word


class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not curr.children[idx]:
                curr.children[idx] = Node(c)
            curr = curr.children[idx]
        curr.end_of_word = True

    def search(self, word: str) -> bool:
        """
        Explanation to be filled.
        """
        def dfs(curr, word):
            for i, c in enumerate(word):
                if c == '.':
                    for n in curr.children:
                        if n and dfs(n, word[i + 1:]):
                            return True
                    return False
                    
                else:
                    idx = ord(c) - ord('a')
                    if not curr.children[idx]:
                        return False
                    else:
                        curr = curr.children[idx]
            return curr.end_of_word

        return dfs(self.root, word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
