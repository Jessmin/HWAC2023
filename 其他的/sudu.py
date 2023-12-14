import sys
lines = [
'0 9 2 4 8 1 7 6 3',
'4 1 3 7 6 2 9 8 5',
'8 6 7 3 5 9 4 1 2',
'6 2 4 1 9 5 3 7 8',
'7 5 9 8 4 3 1 2 6',
'1 3 8 6 2 7 5 9 4',
'2 7 1 5 3 8 6 4 9',
'3 8 6 9 1 4 2 5 7',
'0 4 5 2 7 6 8 3 1',
]
# lines =[]
# for i in range(9):
#     lines.append(sys.stdin)
board= [[int(x) for x in line.split(' ')] for line in lines]
empty = []
rowFlag = [[0]*9 for _ in range(9)]

colFlag = [[0]*9 for _ in range(9)]
squareFlag = [[[0]*9 for _ in range(3)]*3 for i in range(3)]
for i in range(9):
    for j in range(9):
        if board[i][j] ==0:
            empty.append([i,j])
        else:
            val = board[i][j]-1
            rowFlag[i][val] = 1
            colFlag[j][val] = 1
            squareFlag[i//3][j//3][val] = 1

def dfs(board,empty,rowFlag,colFlag,squareFlag,index,done):
    if index == len(empty):
        for i in range(9):
            print(' '.join(str(x) for x in board[i]))
        done = 1
        return
    x,y = empty[index]
    if done!=1:
        for v in range(9):
            if rowFlag[x][v] or colFlag[y][v] or squareFlag[x//3][y//3][v]:
                continue
            rowFlag[x][v] = colFlag[y][v] = squareFlag[x//3][y//3] = 0
            board[x][y] = v+1
            dfs(board,empty,rowFlag,colFlag,squareFlag,index+1,done)
            #回溯
            rowFlag[x][v] = colFlag[y][v] = squareFlag[x//3][y//3] = 1
            board[x][y] =0
        
dfs(board,empty,rowFlag,colFlag,squareFlag,0,0)

    