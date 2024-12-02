class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int iReal = 0;
        int k = 1; // assume at least one unique integer
        for (int iCurr = 0; iCurr < nums.size(); iCurr++){
            int currNum = nums[iCurr];
            if (currNum != nums[iReal]){
                nums[iReal++ + 1] = currNum;
                k++;
            }
        }
        return k;

    }
};
