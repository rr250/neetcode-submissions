class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        v = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
        maxSize=0
        def traverse(m,n, size):
            v[m][n]=1
            if grid[m][n]==0:
                return 0
            a,b,c,d=0,0,0,0
            if v[m-1][n] == 0 and m>0:
                a=traverse(m-1,n,size+1)
            if v[m][n-1] == 0 and n>0:
                b=traverse(m,n-1,size+1)
            if m<len(grid)-1 and v[m+1][n] == 0:
                c=traverse(m+1,n,size+1)
            if n<len(grid[0])-1 and v[m][n+1] == 0:
                d=traverse(m,n+1,size+1)
            # print(m,n,a,b,c,d, size)
            return a+b+c+d+1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if v[i][j]==1:
                    continue
                size = traverse(i,j, 0)
                maxSize=max(maxSize, size)
                # print(i,j,size)
        return maxSize