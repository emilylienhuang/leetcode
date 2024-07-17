class Solution:
    def __init__(self):
        self.memo = {1: 0}
    def integerReplacement(self, n: int) -> int:
        #Memoization
        #Runtime and Spacetime O(logn)
        if n in self.memo:
            return self.memo[n]
        
        if n % 2 == 0:
            self.memo[n] =  1 + self.integerReplacement(n/2)
        else:
            self.memo[n] =  1 + min(self.integerReplacement(n+1), self.integerReplacement(n-1))
        
        return self.memo[n]

