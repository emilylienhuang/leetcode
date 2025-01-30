class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for pos, speed in zip(position, speed):
            cars.append((pos, speed))
        
        stack = []
        cars.sort(reverse=True) # furthest away first processed
        for p, s in cars:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
        
        