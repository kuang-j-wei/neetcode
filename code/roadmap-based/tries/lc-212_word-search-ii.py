from typing import List


class Node:
    def __init__(self):
        self.children = {}
        

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        For each letter, we can identify all its adjacent letters. These
        sequences then will form a chain. So we could have all
        characters be a starting node, then start tracing a chain.

        Since m and n are limited by 12, we can just trace through the
        entire board to construct a trie structure. Then for each node,
        we will put all possible neighboring nodes as its children nodes

        But for each tree path, we have to make sure that a previously
        visited character can't be visited again. This maybe could be
        achieved by creating another 12 by 12 array where for each path
        we keep track of the node that has been visited. But if for each
        path we have to do this once, then that would blow up the space
        complexity. This could maybe be avoided if we do an "inplace"
        memory wiping so only trace through one path at a time then
        backtrack and flipping the visited node back to non-visited
        node.

        Alternatively we could just, for each word, iterate through its
        characters. Then for each character, we assess if we have all
        the necessary neighboring characters.
        """
        self.board = board
        self.constructTrie(board)
        matched_words = []
        for word in words:
            if self.findMatch(word):
                matched_words.append(word)
        return matched_words


    def findMatch(self, word):
        if word[0] in self.starting_points:
            for starting_point in self.start_points[word[0]]:
                if self.findPath(starting_point, word):
                    return True
        return False

    def findPath(self, starting_point, word):
        """
        starting_point is an index pair
        
        Given a starting point and a word, recursively trace through the
        indices.
        """
        curr = self.trie[starting_point]
        for c in word:
            if c not in curr.children:
                return False
            else:
                curr = curr.children
        return True
    
    def constructTrie(self):
        self.trie = {}

        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                char = self.board[r][c]
                self.trie[(r, c)] = Node()
                self.constructPath(self.trie[(r, c)])

    def constructPath(self, node, starting_index):
        """
        Construct a trie given a starting node
        """
        return None