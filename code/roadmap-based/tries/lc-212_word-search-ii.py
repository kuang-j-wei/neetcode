from typing import List


class Node:
    def __init__(self, val=None):
        self.val = val
        self.children = {}
        self.end_of_word = None

    def markEndOfWord(self, word):
        self.end_of_word = word

    def isEndOfWord(self):
        return self.end_of_word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        We will construct tries from each word. This way while we are
        traversing through the board, we can quickly eliminate any path
        that don't already fit an existing trie, and we can stop
        traversing immediately.

        In terms of traversing the board, we will iterate through every
        element of the board and use each as the starting point to
        perform DFS from.

        Time Complexity O(W * L) and O(m * n * 4^L):
            W is words.length, and L is the maximum length of the words.

            Forming the trie involves iterating through all words and
            every character of each word. So the number of operations is
            W * L

            Then we have a nested loop of m * n to use each element on
            the board as a starting point. And inside each starting
            position, we do 4 directions of dfs. And we would perform
            this DFS to at most the length of the longest word, because
            once we exceed the length, we've run through the entire
            depth of the trie, and we would terminate the dfs early.
            So we would at most do this 4x operations L times, so the
            outer loop is O(m * n) then each inner loop is at most
            O(4^L), for a total of O(m * n * 4^L)

        Space Complexity O(W * L) and O(m * n):
            The trie that store the words at worse case be
            O(W * L) as we store every character of as a
            node in the Trie. And for the dfs, we can also at worst
            build a recursive stack that's the full length of all the
            elements in the board since we can't visit a board element
            twice. And the board has m * n elements so the space cost
            is O(m * n). And the visited array itself is also O(m * n)
            in space
        """
        self.board = board
        self.m = len(self.board)
        self.n = len(self.board[0])
        self.visited = [[False for _ in range(self.n)] for _ in range(self.m)]
        self.root = Node()
        self.formTrie(words)

        self.matched_words = []
        for i, row in enumerate(board):
            for j in range(len(row)):
                self.dfs(i, j, self.root)
        return self.matched_words


    def formTrie(self, words):
        for word in words:
            curr = self.root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = Node(c)
                curr = curr.children[c]
            curr.markEndOfWord(word)


    def dfs(self, i, j, curr):
        """
        We will first check if the element requested is out of bounds.

        Then we check whether the element has been visited or not.

        In either cases, we will simply return None to terminate the dfs
        early.

        Then we check if the character that we are on is part of the
        trie or not by checking if we can find this character in the
        current node's children. If we can, then we have a chance of
        advancing to trace more characters, thus we mark this current
        board position as visits and aim to kick off dfs in all four
        directions. But before we do the dfs, we first check whether
        the current chain has already formed a word match. If it did,
        we can first append this word to the matched_words list. And we
        also remove the end_of_word marking from the Trie, so that this
        word doesn't get added again to the matched_words list twice.

        Then we go through dfs in all four directions.

        Once all four directions dfs are done, we set the current board
        position  as unvisited, then the dfs function is over, or in
        other words, backtracked.
        """
        if i >= self.m or j >= self.n or i < 0 or j < 0 or self.visited[i][j]:
            return None

        element = self.board[i][j]

        if element not in curr.children:
            return None

        self.visited[i][j] = True
        if curr.children[element].isEndOfWord():
            self.matched_words.append(curr.children[element].isEndOfWord())  # found a match, directly append
            curr.children[element].markEndOfWord(None)
        self.dfs(i + 1, j, curr.children[element])
        self.dfs(i - 1, j, curr.children[element])
        self.dfs(i, j + 1, curr.children[element])
        self.dfs(i, j - 1, curr.children[element])
        self.visited[i][j] = False



if __name__ == '__main__':
    board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    words = ["oath","pea","eat","rain"]

    s = Solution()
    s.findWords(board, words)
