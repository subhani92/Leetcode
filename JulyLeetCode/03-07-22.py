class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        
        if len(nums) <2:
            return len(nums)
        
        
        up_dp = [0 for _ in (nums)]
        down_dp = [0 for _ in (nums)]
        
        for i in range(1, len(nums)):
            for j in range(0,i, 1):
                
                if nums[i] > nums[j]:
                    
                    up_dp[i] = max(up_dp[i], down_dp[j]+1)
                    
                elif nums[i] < nums[j]:
                    down_dp[i] = max(down_dp[i], up_dp[j]+1)
                    
        
        return 1 + max(down_dp[len(nums)-1], up_dp[len(nums)-1])