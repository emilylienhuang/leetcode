class Solution {
    public int majorityElement(int[] nums) {
        Arrays.sort(nums);
        int times = nums.length / 2;
        int currCount = 1;
        for (int i = 0; i < nums.length - 1; i++){
            if (nums[i] == nums[i + 1]){
                currCount++;
            } else {
                currCount = 1;
            }
            if (currCount > times){
                return nums[i + 1];
            }
        }
        return nums[0];
    }
}
