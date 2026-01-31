class Node:
    def __init__(self, char=None, children=None):
        self.char = char
        self.children = [0] * 27


class Trie:
    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        curr = self.root
        
        for c in word:
            print(f"Currently on {curr.char}")
            
            char_idx = ord(c) - ord('a')
            if not curr.children[char_idx]:
                print(f"{c} is not a child of {curr.char}, adding it")
                curr.children[char_idx] = Node(c)
                print(f"setting {curr.char}'s last children element to 1 to indicate that it now has a child")
                curr.children[-1] = 1
                curr = curr.children[char_idx]
                print(f"Set curr to {curr.char}")
            else:
                print(f"{c} is already a child of {curr.char}, advancing curr to {c}")
                curr = curr.children[char_idx]
        print(f'Last element is {curr.char}, and {curr.char}.children[-1] = {curr.children[-1]}')
        print('\n')

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            # print(f"Seaching {c} character")
            char_idx = ord(c) - ord('a')
            if not curr.children[char_idx]:
                print(f"{c} character not found, returning False")
                return False
            else:
                print(f"{c} character found, advancing curr to {curr.children[char_idx].char}")
                curr = curr.children[char_idx]
        print(f"Iterated over all of {word}, now checking if {curr.char}.children[-1] is 0: {curr.children[-1]}\n")
        return True if curr.children[-1] == 0 else False

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        
        for c in prefix:
            char_idx = ord(c) - ord('a')
            if not curr.children[char_idx]:
                return False
            else:
                curr = curr.children[char_idx]
        return True
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)