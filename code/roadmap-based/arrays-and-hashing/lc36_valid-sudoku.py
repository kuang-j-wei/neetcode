from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Solution:
            The goal is just to iterate over the 81 items only once

            We can use a hashmap to track row-check, column-check, and
            square-check

            So at every element, we simply check if this number has
            appeared in the row, column, and square hashmap before
 
        Time Complexity: O(1)
            Or to be precise, 9x9 = 81 times. If the sudoku were to grow
            to n, then the time complexity would be O(n^2)

        Space Complexity: O(1)
            Again all the hashmaps could at most occupy 81 so doesn't
            scale. But if the sudoku dimension were to grow to n then
            the space complexity also would be O(n^2)

            While each hashmap can only has up to n keys, each of its
            sub-hashmap could then take up another n keys, so the
            complexity grows as O(n^2)
        """
        def row_col_to_square(i, j):
            return (i // 3) * 3 + j  // 3
        row_check = {i: set() for i in range(9)}
        col_check = {i: set() for i in range(9)}
        square_check = {i: set() for i in range(9)}

        for i in range(0, 9):  # row
            for j in range(0, 9):  # col
                val = board[i][j]
                if val == '.':
                    continue
                
                square_idx = row_col_to_square(i, j)
                if (
                    val in row_check[i]
                    or val in col_check[j]
                    or val in square_check[square_idx]
                ):
                    return False  
                else:
                    row_check[i].add(val)
                    col_check[j].add(val)
                    square_check[square_idx].add(val)
        return True

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Time Complexity: O(1)
            It's really 81 operations 3 times, but doesn't actually
            grow with any kind of input since it's always a 9x9 grid
        Space Complexity: O(1)
            Again the hashmap check always at most only take up 10
            elements
        """
        for row in board:
            row_check = {}
            for col_element in row:
                if col_element == ".":
                    continue

                if col_element in row_check:
                    print(f'found row failed for {col_element}')
                    return False
                else:
                    row_check[col_element] = 1

        for i in range(9):
            col_check = {}
            for row in board:
                val = row[i]
                if val  == ".":
                    continue

                if val in col_check:
                    print(f'found column failed for {val}')
                    return False
                else:
                    col_check[val] = 1

        for i in range(0, 9, 3):
            for j in range(0, 9 ,3):
                square_check = {}

                for ii in range(3):
                    for jj in range(3):
                        val = board[i + ii][j + jj]

                        if val == '.':
                            continue

                        if val in square_check:
                            print(f"Found square failed at [{i}+{ii}][{j}+{jj}]")
                            return False
                        else:
                            square_check[val] = 1
        return True


if __name__ == '__main__':
    s = Solution()
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    s.isValidSudoku(board)