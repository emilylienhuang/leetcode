class Solution {
    public int removeDuplicates(int[] nums) {
        int k = 1;
        int iReal = 0;
        for (int iCurr = 0; iCurr < nums.length; iCurr++){
            if (nums[iCurr] != nums[iReal]){
                nums[iReal++ + 1] = nums[iCurr];
                k++;
            }
        }
       
        return k;
    }
}
