class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        vector = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        already_explored = set()
        
        def is_valid(index):
            if r > index[0] > -1 and c > index[1] > -1:
                return True
            return False
        
        def change_board(path):
            for index in path:
                board[index[0]][index[1]] = "X"
        
        def helper(index, path):
            
            res = True
            for vec in vector:
                new_index = (vec[0]+index[0], vec[1]+index[1])
                if new_index in path or (is_valid(new_index) and board[new_index[0]][new_index[1]] == "X"):
                    continue
                elif not is_valid(new_index):
                    return False
                path.add(new_index)
                res = res and helper(new_index, path)
            return res
        
        r = len(board)
        c = len(board[0])
        for i in range(r):
            for j in range(c):
                path = set()
                path.add((i, j))
                if board[i][j] != "X" and helper((i, j), path):
                    change_board(path)
        return board