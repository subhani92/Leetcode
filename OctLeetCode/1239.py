class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        ## get all valid concatenation 
        ## o yeah brute-force can work for the given contrains
        
        self.ans = 0

        def solve(idx, temp = []):
            concating = "".join(temp)
            
            if len(concating) != len(set(concating)):
                return 
            
            self.ans = max(self.ans, len(concating) )
            # print(temp)
            
            for i in range(idx, len(arr)):
                temp.append(arr[i])
                solve(i+1, temp )
                temp.pop()

        
        solve(0)
        
        # print(self.ans)
        
        return self.ans
            
