class Solution {
    public boolean canJump(int[] nums) {
        int maxReach = 0;
        for (int i = 0; i < nums.length - 1; i++){
            if (i > maxReach){
                return false;
            }
            maxReach = Math.max(nums[i] + i, maxReach);
        }
        return maxReach >= nums.length - 1;
    }
}
