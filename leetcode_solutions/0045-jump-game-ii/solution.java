class Solution {
    public int jump(int[] nums) {
        int jumps = 0;
        int furthest = 0;
        int end = 0;
        for (int i = 0; i < nums.length-1; i++){
            furthest = Math.max(nums[i] + i, furthest);
            if (furthest >= nums.length - 1){
                jumps++;
                return jumps;
            }
            if (i == end){
                jumps++;
                end = furthest;
            }
        }
        return jumps;
    }
}
