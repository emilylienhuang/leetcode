class Solution:
    def nthUglyNumber(self, n: int) -> int:
        '''
        TOP PRIORITY: helper function for is ugly
        n == 1 edge case -> could possibly be addressed with proper coding
        num = 0 # might have to address starting at 0 later
        curr_ugly = num
        while n > 0:
            if isUgly(num):
                n -= 1 
                curr_ugly = num
            num += 1
        '''
        if n == 1:
            return 1
        
        num = 1
        curr_ugly_num = 0
        count = 0
        while count < n:
            # O(n) time
            if self.isUgly(num):
                curr_ugly_num = num
                count += 1
            num += 1
        return curr_ugly_num

    # runs in O(n)
    # runs in space O(n)   
    def isUgly(self, n):
        prime_factors = []
        # Print the number of two's that divide n
        while n % 2 == 0:
            prime_factors.append(2)
            n = n // 2
                
        # n must be odd at this point
        # so a skip of 2 ( i = i + 2) can be used
        for i in range(3,int(math.sqrt(n))+1,2):
                
            # while i divides n , print i ad divide n
            while n % i== 0:
                prime_factors.append(i)
                n = n // i
                    
        # Condition if n is a prime
        # number greater than 2
        if n > 2:
            prime_factors.append(n)
        
        selected = [1, 2, 3, 5]
        for prime in prime_factors:
            if prime not in selected:
                return False
        return True
            
    
        