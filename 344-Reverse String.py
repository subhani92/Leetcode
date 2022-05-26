class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
    
        def solve(s, l, r):
            
            if l>=r:
                return
            
            ##process
            s[l], s[r] = s[r], s[l]
                
            return solve(s, l+1, r-1)
            
        l = 0
        r = len(s)-1
        return solve(s, 0, r)
        