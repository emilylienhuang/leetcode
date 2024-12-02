class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int p_write = 0;
        int p_read = 0;
        while(p_read < nums.size()){
            if (nums[p_read] != val){
                nums[p_write++] = nums[p_read];
            }
            p_read++;
        }
        return p_write;
    }
};
