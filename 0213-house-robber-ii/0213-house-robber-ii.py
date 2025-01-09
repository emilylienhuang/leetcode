class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def getMoney(arr):
            prev_rob, max_rob = 0,0
            for num in arr:
                tmp = max(prev_rob + num, max_rob)
                prev_rob = max_rob
                max_rob = tmp
            return max_rob
        
        return max([getMoney(nums[1:]), getMoney(nums[:-1]), nums[0]])