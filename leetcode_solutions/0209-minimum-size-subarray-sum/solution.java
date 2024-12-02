class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int left = 0;
        int count = 0;
        int minSize = Integer.MAX_VALUE;
        for (int right = 0; right < nums.length ; right++){
            count += nums[right];
            while (count >= target){
                minSize = Math.min(minSize, (right - left + 1));
                count -= nums[left++];
            }
        }

        return minSize == Integer.MAX_VALUE ? 0 : minSize;
    }
}
