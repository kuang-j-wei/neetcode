from typing import List


class Node:
    def __init__(self):
        self.children = [0] * 26
        

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