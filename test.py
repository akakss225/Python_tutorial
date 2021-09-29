def solution(board, moves):
    answer = 0
    for i in board:
        i.reverse()
    return board


board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

# 4
print(solution(board, moves))