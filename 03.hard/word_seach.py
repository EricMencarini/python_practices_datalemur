#https://datalemur.com/questions/python-word-search
'''
Given an m x n grid of characters board and a string word, return True if word exists in the grid.

For the word to exist, you must be able to construct it from a sequence of cells, where each is adjacent (horizontally or vertically, but not diagonal) to the next one in the sequence. The same cell may not be used twice.

Example #1
Word Search DataLemur Example

Input: board = [['A', 'L', 'E', 'D'], ['E', 'F', 'M', 'H'], ['I', 'R', 'U', 'L']] , word = "LEMUR"
'''
board = [['A', 'L', 'E', 'D'], ['E', 'F', 'M', 'H'], ['I', 'R', 'U', 'L']] 
word = "LEMUR"

from collections import Counter

def exist(board, word):
    ROWS, COLS = len(board), len(board[0])
    word_count = Counter(word)
    board_count = Counter(ch for row in board for ch in row)

    for ch, cnt in word_count.items():
        if board_count[ch] < cnt:
            return False

    if board_count[word[0]] > board_count[word[-1]]:
        word = word[::-1]

    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    visited = set()

    def dfs(i, j, k):
        if k == len(word):
            return True
        if (
            i < 0 or i >= ROWS or j < 0 or j >= COLS or
            board[i][j] != word[k] or
            (i, j) in visited
        ):
            return False

        visited.add((i, j))
        for di, dj in directions:
            if dfs(i + di, j + dj, k + 1):
                return True
        visited.remove((i, j))
        return False

    for i in range(ROWS):
        for j in range(COLS):
            if board[i][j] == word[0] and dfs(i, j, 0):
                return True

    return False