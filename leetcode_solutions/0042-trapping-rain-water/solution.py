class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = height[0]
        right_max = height[len(height) - 1]
        left_ptr = 0
        right_ptr = len(height) - 1
        water = 0

        while (left_ptr < right_ptr):
            if (height[left_ptr] <= height[right_ptr]):
                if (height[left_ptr] < left_max):
                    water += left_max - height[left_ptr]
                else:
                    left_max = height[left_ptr]
                left_ptr += 1
            else:
                if (height[right_ptr] < right_max):
                    water += right_max - height[right_ptr]
                else:
                    right_max = height[right_ptr]
           
                right_ptr -= 1
        return water
