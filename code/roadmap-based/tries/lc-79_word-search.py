from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        We can iteratively search through the entire board by treating
        every board position as a possible starting position, then then
        then from there we perform dfs to traverse all four directions.
        
        We can terminate early for a dfs sequence for any of the
        following reasons:
            * The current sequence already doesn't match up with word
            * Out of bound of the board
            * Run into a previously visited node
        
        In the DFS, we make this early termination (or early success)
        to be indicated by using an `OR` operand across all four
        directions, and then returning the final logic as determined by
        the result of all four directions. This way, as long as one
        direction found a word match, we return True up the dfs stack,
        which then trigger `exist` to return True.

        Lastly, we also set the current node visited array to be False
        once we are done with the current position dfs so when we
        backtrack the visited nodes are marked as unvisited again so
        future explorations could go through them.

        Time Complexity: O(m * n * 4^L)
            We treat each board position as a starting point. But the
            dfs in each direction could at most go to the length of the
            word before it's terminated. So the 4 branches could at most
            occur L times, thus adding a 4^L complexity.
        
        Space Complexity: O(m * n + L)
            The visited array takes up an additional O(m * n), and the
            recursive stack can at most grow to height L
        """
        self.board = board
        self.m = len(self.board)
        self.n = len(self.board[0])
        self.word = word
        self.visited = [[False for _ in range(self.n)] for _ in range(self.m)]
        
        for i, row in enumerate(board):
            for j in range(len(row)):
                if self.dfs(i, j, 0):
                    return True
        return False
    
    def dfs(self, i, j, word_idx):
        if i < 0 or j < 0 or i >= self.m or j >= self.n or word_idx >= len(self.word):
            return False
        
        if self.visited[i][j]:
            return False
        
        element = self.board[i][j]
        if element != self.word[word_idx]:
            return False
        elif word_idx == len(self.word) - 1:
            return True
        
        self.visited[i][j] = True
        search_result = (
            self.dfs(i + 1, j, word_idx + 1) or
            self.dfs(i - 1, j, word_idx + 1) or
            self.dfs(i, j + 1, word_idx + 1) or
            self.dfs(i, j - 1, word_idx + 1)
        )
        
        self.visited[i][j] = False
        return search_result
