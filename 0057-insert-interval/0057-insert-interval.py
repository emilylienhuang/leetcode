class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        Given: an array of intervals in ascending, sorted order
        Output: the intervals with the new added interval in 

        Need: - a for loop to loop over intervals
        - a result vairable to store the intervals

        Edge cases:
        if curr_i[end] < new_i[start]: and append
        if intervals overlap, merged -> curr_i[end] >= new_i[start] merge intervals
        if interval needs to be inserted if curr_i[start] > new_i[end]: add in interval and current interval
        '''
        if not intervals:
            return [newInterval]

        new_start, new_end = newInterval

        res = deque([newInterval])
    
        for c_start, c_end in intervals:
            r_start, r_end = res[-1]
            if  c_end < r_start:
                res.appendleft([c_start, c_end])
            elif c_start > r_end:
                res.append([c_start, c_end])
            else:
                res[-1] = [min(c_start, r_start), max(c_end, r_end)]
        return list(res)
            
