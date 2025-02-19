class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        # use bellman-ford algorithm

        prices = [float('inf')] * n
        prices[src] = 0

        for _ in range(k + 1):
            tempArr = prices[:]
            for s, d, p in flights:
                if tempArr[s] == float('inf'):
                    continue

                newPrice = p + prices[s]
                if newPrice < tempArr[d]:
                    tempArr[d] = newPrice
            prices = tempArr
        
        return -1 if prices[dst] == float('inf') else prices[dst]