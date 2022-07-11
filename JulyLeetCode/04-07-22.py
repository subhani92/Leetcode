class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        
        ## give candy from right to left and the left to right
        
        if not ratings:
            return ratings
        
        n = len(ratings)
        
        
        left_to_right = [1 for _ in range(n)]
        
        right_to_left = [1 for _ in range(n)]
        
#         left_to_right[0] = 1
#         right_to_left[n-1] = 1
        
        for i in range(1, len(ratings)):
            
            if ratings[i] >  ratings[i-1]:
                left_to_right[i] =left_to_right[i-1] +  1
            
        for i in range(n-2, -1, -1):
            
            if ratings[i] >  ratings[i+1]:
                right_to_left[i] =right_to_left[i+1]+ 1
                
        
            
        ans = 0
        for i in range(n):
            ans += max(left_to_right[i], right_to_left[i])
            
        return ans