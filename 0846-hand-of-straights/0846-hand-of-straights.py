class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        def filledGroup(arr):
            return (len(arr) == groupSize)
        hand.sort()
        q = deque(hand)
        res = [[] for _ in range(groupSize)]
        group_idx = 0
        default = 0
        while q: 
            num = q.popleft()
            while res[group_idx] and num <= res[group_idx][-1] and group_idx < len(res):
                group_idx += 1
            
            res[group_idx].append(num)
            if filledGroup(res[group_idx]):
                default = group_idx + 1
            group_idx = default
        
        for group in res:
            if len(group) != groupSize:
                return False
        return True
            


