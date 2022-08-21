from collections import defaultdict

vectors = [(0, 1), (1, 0), (0, -1), (-1, 0)]

memo = defaultdict(lambda: None)

class Solution:
    def depthSearch(self, word: str, alreadyVisited, indexes):
        if len(word) == 0 or (len(word) == 1 and word[0] == self.board[indexes[0]][indexes[1]]):
            return True
        if memo[(indexes, word)] != None:
            return memo[(indexes, word)]
        if self.board[indexes[0]][indexes[1]] == word[0]:
            for vector in vectors:
                newIndexes = (vector[0] + indexes[0], vector[1] + indexes[1])
                if 0 <= newIndexes[0] < self.height and 0 <= newIndexes[1] < self.width and alreadyVisited.get(newIndexes) is None:
                    alreadyVisited[indexes] = True
                    result = self.depthSearch(word[1:], alreadyVisited, newIndexes)
                    del alreadyVisited[indexes]
                    if result:
                        memo[(newIndexes, word)] = True
                        return True
        memo[(indexes, word)] = False
        return False
    
    

    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        
        visited = set()
        
        def is_valid(r, c):
            if r < 0 or r >= row or c < 0 or c >= col:
                return False
            return True
        
        def helper(word_i, r, c):
            
            if word_i == len(word):
                return True
            
            if (r, c) in visited:
                return False

            if not is_valid(r, c):
                return False
            
            if board[r][c] != word[word_i]:
                return False
            
            visited.add((r, c))
            res = helper(word_i + 1, r+1, c) or helper(word_i + 1, r-1, c) or helper(word_i + 1, r, c+1) or helper(word_i + 1, r, c-1)
            visited.remove((r, c))
            return res
                    
        for i in range(row):
            for j in range(col):
                if helper(0, i, j):
                    return True
        return False
        
        self.board = board
        self.height = len(board)
        self.width = len(board[0])
        for i in range(0, self.height):
            for j in range(0, self.width):
                result = self.depthSearch(word, {}, (i, j))
                if result:
                    return True
        return False

    def __init__(self):
        self.board = None
        self.height = 0
        self.width = 0