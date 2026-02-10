from typing import List


class Node:
    def __init__(self):
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
        
        TODO:
            * Add unmarking visited logic
            * Collect word
            * Remove word from trie
        """
        self.board = board
        self.m = len(self.board)
        self.n = len(self.board[0])
        self.visited = [[False] * self.n for _ in range(self.m)]
        self.root = Node()
        self.formTrie(words)

        self.matched_words = []
        for i, row in enumerate(board):
            for j in range(len(row)):
                if not dfs(i, j, self.root):
                    break
                else:
                    self.matched_words.append(word)
                
        return self.matched_words


    def formTrie(self):
        for word in words:
            curr = self.root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = Node()
                curr = curr.children[c]
            curr.markEndOfWord(word)

    def dfs(self, i, j, curr):
        element = self.board[i][j]
        self.visited[i][j] = True
        if element not in curr.children:
            return False
        elif element in curr.children and curr.children[element].isEndOfWord():
            return True
        elif element in curr.children:
            if i + 1 < self.m and not self.visited[i + 1][j]:
                return dfs(i + 1, j, curr.children[element])
            if i - 1 >= 0 and not self.visited[i - 1][j]:
                return dfs(i - 1, j, curr.children[element])
            if j + 1 < self.n and not self.visited[i][j + 1]:
                return dfs(i, j + 1, curr.children[element])
            if j - 1 >= 0 and not self.visited[i][j - 1]:
                return dfs(i, j - 1, curr.children[element])
        else:
            return False
