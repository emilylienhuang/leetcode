class Solution {
    public int dominantIndex(int[] nums) {
        int max = 0;
        int iMax = 0;
        for (int i = 0; i < nums.length; i++){
            if (max < nums[i]){
                max = nums[i];
                iMax = i;
            }
        }
        
        for (int num : nums){
            if (max != num && max < (2 * num)){
                return -1;
            }
        }
        return iMax;
    }
}
