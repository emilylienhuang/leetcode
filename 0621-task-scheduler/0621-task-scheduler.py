class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        Understanding: I need to run all tasks in task
        They must be separated by n for tasks of the same label
        I must return the MINIMUM number of intervals needed to run all tasks

        Helpful:
        -Heap like hash structure to keep track of frequencies of task
        -Approach by Greedy at first, run the largest tasks up front
        -Choose the next smallest task to run subtracting from idle time
        - return the idle time + len(tasks)

        Edge cases:
        n == 0:
            just run all tasks
        '''

        if n == 0:
            return len(tasks)
        
        task_freq = [0] * 26 # 26 letters in the alphabet

        for task in tasks:
            task_freq[ord(task) - ord('A')] += 1
        
        task_freq.sort() # O(26 log 26)

        max_freq = task_freq.pop()
        idle_time = (max_freq - 1) * n

        # treat like a heap
        while task_freq and task_freq[-1] > 0:
            curr_task = task_freq.pop()
            idle_time -= min(max_freq - 1, idle_time)
        
        idle_time = max(idle_time, 0)
        return idle_time + len(tasks)
