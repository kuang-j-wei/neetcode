class Node:
    def __init__(self, char=None, children=None, end_of_word=False):
        self.char = char
        self.children = [None] * 26
        self.end_of_word = end_of_word


class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        """
        Time Complexity: O(n)
            We would have to loop through every char of word
        
        Space Complexity: O(n)
            In the word case, the entire character sequence is brand new
            then we would have to create n new nodes.
        """
        curr = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not curr.children[idx]:
                curr.children[idx] = Node(c)
            curr = curr.children[idx]
        curr.end_of_word = True

    def search(self, word: str) -> bool:
        """
        When we encounter a '.', then we need to search through all
        the children of the current node, and see if any of the children
        nodes can successfully solve for the rest of the word, skipping
        the current character. Because the current character can be of
        any node now, what we care about is the next character and
        whether the current node has a child that can continue on to
        solve the problem. So we will go with a recursive solution,
        where we call the function itself when we encounter a '.' char.

        Lastly, once we've searched through all characters and every
        char has been found, we just need to check whether the last
        char is the end of a word.

        Time Complexity: O(n) for no dots, O(26^k x n) for k = number of
                         dots
            Every character is scanned once. But if there is a '.'
            encountered, we have to branch out to all 26 children of the
            current node, which creates another O(n) time complexity. So
            the total is O(26 * n) for every '.'
        
        Space Complexity: O(n)
            No additional space is used, since the problem states that
            at most two '.' characters could be found in the input
            word, so the recursive stack could at most grow to 2.

            But because the slicing `word[i + 1:]`, it creates a copy
            of the slice that gets passed to `dfs`. So this still
            creates an additional O(n) space complexity
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
