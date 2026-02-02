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

    def search(self, word: str) -> bool:
        """
        For '.', it doesn't matter what the current node is, as long as
        it's not empty. If it's empty, then we return False (so we might
        need a "children empty" indicator). And we would need to move
        onto the next character after '.'. So we would need to skip the
        current layer of the Trie, and search the next. We could do this
        by iterating through all the current node that was previous on
        '.' and search through their children. If any of their child
        contains this character, then we can continue to iterate
        forward.
        """
        curr = self.root
        prev_is_dot = False
        consecutive_dots = False
        consecutive_dots_found = False
        for c in word:
            if consecutive_dots:
                idx = ord(c) - ord('a')
                
                for n in curr.children:
                    if n:
                        for nc in n.children:
                            if nc and nc.children[idx]:
                                consecutive_dots_found = True
                                consecutive_dots = False
                                prev_is_dot = False
                                curr = nc.children[idx]
                                break
                    if consecutive_dots_found:
                        break    

            elif prev_is_dot and c != '.':
                idx = ord(c) - ord('a')
                for n in curr.children:
                    if n and n.children[idx]:
                        curr = n.children[idx]
                        prev_is_dot = False
                        break
            elif prev_is_dot and c == '.':
                consecutive_dots = True
                continue
            else:                            
                if c == '.':
                    prev_is_dot = True
                    continue                    
                    
                idx = ord(c) - ord('a')
                if not curr.children[idx]:
                    return False
                else:
                    curr = curr.children[idx]
        return True 


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
