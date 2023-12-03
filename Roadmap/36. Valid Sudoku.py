class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # key = (r /3, c /3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True
###############################################################################

###############################################################################
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        has = {}
        for i in range(1,10):
            has[str(i)]=0
        has[str('.')]=0
        


        for i in range(0,9) :
            o=has.copy()
            for j in range(0,9) :
                if str(board[i][j]) !=str('.') and o[str(board[i][j])]==1:
                    return False
                o[str(board[i][j])]=1

        for j in range(0,9):
            o=has.copy()
            for i in range(0,9):
                if str(board[i][j]) !=str('.') and o[str(board[i][j])]==1: 
                    return False
                o[str(board[i][j])]=1
        
        for k in range(3,10,3):
            for l in range(3,10,3):
                o=has.copy()
                for i in range(k-3,k):
                    print(" ")
                    for j in range(l-3,l):
                        print("{i}{j}".format(i=i,j=j))
                        
                        if str(board[i][j]) !=str('.') and o[str(board[i][j])]==1:
                            
                            print(o)
                            return False
                        o[str(board[i][j])]=1
        return True
