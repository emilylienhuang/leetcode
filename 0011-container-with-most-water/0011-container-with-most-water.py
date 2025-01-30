class Solution:
    def maxArea(self, height: List[int]) -> int:
        # simple area = length * width
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            area = 0
            if height[left] < height[right]:
                area = height[left] * (right - left)
                left += 1
            else:
                area = height[right] * (right - left)
                right -= 1
            max_area = max(area, max_area)
        return max_area
            