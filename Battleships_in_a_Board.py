class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        def ifvisited(board,visited,i,j):
            visited[i][j]=1
            p=i
            while p+1<len(board):
                p+=1
                if board[p][j]=='X':
                    visited[p][j]=1
                else:
                    break
            while j+1<len(board[0]):
                j+=1
                if board[i][j]=='X':
                    visited[i][j]=1
                else:
                    break                   
        visited=[[0 for i in range(len(board[0]))] for j in range(len(board))]
        count=0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='X' and visited[i][j]==0:
                    count+=1
                    ifvisited(board, visited, i, j)
        return count

class Solution1(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        count=0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='X' and (i==0 or board[i-1][j]=='.') and (j==0 or board[i][j-1]=='.'):
                    count+=1
        return count
    
s=Solution1()
board=[[ 'X', '.', '.', 'X' ], [ '.', '.', '.', 'X'], ['.', '.', '.', 'X' ]]
print s.countBattleships(board)