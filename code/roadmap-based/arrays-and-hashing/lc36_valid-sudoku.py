from typing import List


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