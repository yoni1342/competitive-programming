class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
       
        subBox = [[]for _ in range(9)]
        col = defaultdict(list)
        row = defaultdict(list)
        n = len(board)
        for i in range(n):
            for j in range(n):
                if board[i][j].isdigit():
                    col[j].append(board[i][j])
                    row[i].append(board[i][j])

                    if j>=0 and j<=2:
                        if i>=0 and i<=2:
                            subBox[0].append(board[i][j])
                        elif i>=3 and i<=5:
                            subBox[1].append(board[i][j])
                        elif i>=6 and i<=8:
                            subBox[2].append(board[i][j])
                    elif j>=3 and j<=5:
                        if i<=2:
                            subBox[3].append(board[i][j])
                        elif i>=3 and i<=5:
                            subBox[4].append(board[i][j])
                        elif i>=6 and i<=8:
                            subBox[5].append(board[i][j])
                    elif j>=6 and j<=8:
                        if i>=0 and i<=2:
                            subBox[6].append(board[i][j])
                        elif i>=3 and i<=5:
                            subBox[7].append(board[i][j])
                        elif i>=6 and i<=8:
                            subBox[8].append(board[i][j])
        
        for i in col:
            if len(set(col[i])) != len(col[i]):
                return False
        for i in row:
            if len(set(row[i])) != len(row[i]):
                return False
        for i in subBox:
            if len(set(i))!=len(i):
                return False
        return True
            

                        