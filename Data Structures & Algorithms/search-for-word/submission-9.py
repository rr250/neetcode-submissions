class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m=len(board)
        n=len(board[0])
        # print(v)
        def traverse(i,j,k,v):
            # if v[i][j]==1:
            #     return False
            # v[i][j]=True
            print(i,j,k, word[k], board[i][j],v)
            if (i,j) in v:
                return False
            if k==len(word) or (word[k] == board[i][j] and k==len(word)-1):
                return True
            if word[k] == board[i][j]:
                return (traverse(i-1,j,k+1,v+[(i,j)]) if i>0 else False) or (traverse(i,j-1,k+1,v+[(i,j)]) if j>0 else False) or (traverse(i+1,j,k+1,v+[(i,j)]) if i<len(board)-1 else False) or (traverse(i,j+1,k+1,v+[(i,j)]) if j<len(board[0])-1 else False)
            else:
                return False
        for i in range(m):
            for j in range(n):
                if traverse(i,j,0,[]):
                    return True
        return False
        