class Node:
    def __init__(self, char=None, children=None):
        """
        Attributes:
            char: str
                It's the character that a character represents
            children: list
                It's a list of size 27, where the element can either be
                of a Node object or an integer of 0 or 1. The 1st to
                26th element represents whether it has a child of a
                specific character. The last element will denote whether
                this current Node is the last character of a word, and
                if so, this last element will be of value 1.
        """
        self.char = char
        self.children = [0] * 27


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        """
        Starting from the root, we will start to iterate through the
        input word character by character. If the current character is
        not an existing child of the root node, which can be determined
        by accessing the element that this character represents in the
        root node's children list, then we will create a new Node object
        with this character and add it to the corresponding element of
        the children list. Then we advance the curr pointer to the
        element that's represented by this character. Once we've
        iterated through the entire list, for the last character, we
        denote the last element of its `children` node to be 1,
        indicating that this is the end of a word. This feature will
        then be used by the `search` method in order to see if a
        precise word has been matched.

        Time Complexity: O(n) where n is the length of the input word
            We will need to iterate over every character in this input
            word
        Space Complexity: O(n)
            If a word is a brand new word with no overlapping characters
            at all with what are currently available in the Trie, then
            we would need to add n new Nodes, thus growing the space
            needed by O(n).
        """
        curr = self.root
        
        for c in word:
            char_idx = ord(c) - ord('a')
            if not curr.children[char_idx]:
                curr.children[char_idx] = Node(c)
                curr = curr.children[char_idx]
            else:
                curr = curr.children[char_idx]
        curr.children[-1] = 1

    def search(self, word: str) -> bool:
        """
        As we iterate over every character of `word`, if we don't find
        a character in the Trie, then we can immediately return False.
        Otherwise, once we've iterated over all characters, we also have
        to check the very last element whether it has its "end of word"
        indicator set to 1. If not, it just means this is part of a word
        therefore we have to return False.

        Time Complexity: O(n) where n is the length of the input word
            We will need to iterate over every character in this input
            word
        Space Complexity: O(1)
            No additional space is used
        """
        curr = self.root
        for c in word:
            char_idx = ord(c) - ord('a')
            if not curr.children[char_idx]:
                return False
            else:
                curr = curr.children[char_idx]
        return True if curr.children[-1] else False

    def startsWith(self, prefix: str) -> bool:
        """
        Same implementation logic to the `search` method. Except that
        we don't have to check for the last character's "end of word"
        indicator since we don't need it to be a complete word.

        Time Complexity: O(n) where n is the length of the input prefix 
            We will need to iterate over every character in this input
            word
        Space Complexity: O(1)
            No additional space is used
        """
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