import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        primes = [2,3,5]
        ugly_heap = [1]
        visited = set()
        visited.add(1)
        for _ in range(n):
            curr = heapq.heappop(ugly_heap)
            for prime in primes:
                new_ugly = curr * prime
                if new_ugly not in visited:
                    heapq.heappush(ugly_heap, new_ugly)
                    visited.add(new_ugly)
        return curr