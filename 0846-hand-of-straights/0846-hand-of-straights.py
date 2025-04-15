class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        num_count = Counter(hand)
        hand.sort()
        for num in hand:
            if num_count[num]:
                for i in range(num, num + groupSize):
                    if not num_count[i]:
                        return False
                    num_count[i] -= 1
        return True