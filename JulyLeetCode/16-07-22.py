class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        memo = {}
        def solve(m, n , N, i, j):
            if i ==m or j ==n or i <0 or j <0:
                return 1

            if N==0:
                return 0 
            
            if (m,n, i, j, N) in memo:
                return memo[(m,n, i, j, N)] %  1000000007
            
            ans = solve(m,n, N-1, i-1, j) + solve(m,n, N-1, i+1, j)+ solve(m,n, N-1, i, j+1)+ solve(m,n, N-1, i, j-1)
            memo[(m,n, i, j, N)] = ans %  1000000007

            return ans % 1000000007
                    
                    
        return solve(m,n, maxMove, startRow, startColumn)