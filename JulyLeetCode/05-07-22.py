class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        
        if not nums:
            return 0 
        
        ans =0 
        
        unique = set(nums)
        
        for num in nums:
            if num-1 not in unique:
                
                curr = num
                streak =1
                
                while curr +1 in unique:
                    curr+=1
                    streak +=1
                print(num, streak)
                ans = max(ans, streak)
                

            
        return ans
            
            
            