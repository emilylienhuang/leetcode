class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0
        left, right = 0, len(height) -1
        max_height_left, max_height_right = height[left], height[right]
        while left < right:
            if height[left] < height[right]:
                max_height_left = max(max_height_left, height[left])
                total_water += (max_height_left - height[left])
                left += 1
            else:
                max_height_right = max(max_height_right, height[right])
                total_water += (max_height_right - height[right])
                right -= 1
        return total_water