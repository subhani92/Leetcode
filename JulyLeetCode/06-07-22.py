class Solution:
    def fib(self, n: int) -> int:
        
        if n ==0:
            return 0
        if n==1:
            return 1
        
        
        a, b = 1,0
        for _ in range(2, n+1):
            temp = a 
            a = a+b
            b = temp
            
        return a