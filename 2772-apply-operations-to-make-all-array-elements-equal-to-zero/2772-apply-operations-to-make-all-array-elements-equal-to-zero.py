class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        operation = [0] * (n + 1)  # Difference array
        prefix_sum = 0

        for i in range(n):
            prefix_sum += operation[i]  # Apply effect of previous operations
            current = nums[i] - prefix_sum  # Remaining decrements needed

            if current < 0:  
                return False  # Over-decremented, impossible case

            if current > 0:
                if i + k > n:  
                    return False  # Cannot apply operation beyond array bounds
                operation[i + k] -= current  # Mark end of effect
            prefix_sum += current  # Apply current decrements
        
        return True