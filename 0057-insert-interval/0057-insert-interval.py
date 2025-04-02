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

        n = len(intervals)
        i = 0
        res = []

        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)

        while i < n:
            res.append(intervals[i])
            i += 1
        return res
            
