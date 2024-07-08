class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int sumL = 0;
        int sumR = accumulate(nums.begin(), nums.end(), 0);
        cout<< sumR;
        for (int i = 0; i < nums.size(); i++){
            sumR -= nums[i];
            if (sumL == sumR){
                return i;
            }
            sumL += nums[i];
            
        }
        return -1;
    }
};
