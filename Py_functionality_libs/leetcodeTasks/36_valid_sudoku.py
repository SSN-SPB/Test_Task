# https://leetcode.com/problems/valid-sudoku/description/
# 36. Valid Sudoku completed partly 26-jul-6
board_list = [
 ["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        sample_list = ['1','2','3','4','5','6','7','8','9']
        # append vertical lists
        for v in range(0, 9):
            interim_list = []
            for h in range(0, 9):
                interim_list.append(board[h][v])
            # print(interim_list)
            board.append(interim_list)
        for w in board:
            # print(w)
            for x in sample_list:
                print(f"check {w}")
                print(f"{x} - counted {w.count(x)}")
                if w.count(x) > 1:
                    return False

        return True



def main():
    c = Solution()
    print(f" result : {c.isValidSudoku(board_list)}")


if __name__ == "__main__":
    main()
