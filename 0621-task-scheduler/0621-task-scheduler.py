class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if n == 0:
            return len(tasks)
        freqs = [0] * 26
        for t in tasks:
            freqs[ord(t) - ord('A')] += 1
        freqs.sort()
        max_freq = freqs.pop()
        idle_time = (max_freq - 1)* n
        while idle_time >= 0 and len(freqs) > 0 and freqs[-1] != 0:
            idle_time -= min(freqs.pop(), max_freq - 1)
        idle_time = max(idle_time, 0)
        return len(tasks) + idle_time