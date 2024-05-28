class Solution {
    public void rotate(int[] nums, int k) {
        int n = nums.length;
        k = k % n;
        // reverse the whole thing s.t.each half is in its correct part
        reverse(nums, 0, n-1);

        // reverse the first k elements back to their correct order
        reverse(nums, 0, k-1);

        // reverse the remaining n - k elements back to their correct order
        reverse(nums, k, n-1);
        
    }
    private void reverse(int[] nums, int start, int end){
        while(start < end){
            int temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;
            start++;
            end--;
        }
    }
}
