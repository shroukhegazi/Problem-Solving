class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxes = [set() for i in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    n = int(board[i][j])
					

                    if n in rows[i]:
                        return False
                    else:
                        rows[i].add(n)

				
                    if n in cols[j]:
                        return False
                    else:
                        cols[j].add(n)
                    
		
                    b = i // 3 * 3 + j // 3
                    if n in boxes[b]:
                        return False
                    else:
                        boxes[b].add(n)
	
        return True
