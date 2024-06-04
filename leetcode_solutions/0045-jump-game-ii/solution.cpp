class Solution {
public:
    int jump(vector<int>& nums) {
        // Need the furthest distance, a pointer to the end, and a count of the jumps that we can make
        int farthest = 0;
        int endPtr = 0;
        int jumps = 0;
        for (int i = 0; i < nums.size() - 1; i++){
            // First, update the furthest you can jump
            farthest = max(farthest, nums[i] + i);
            if (farthest >= nums.size() - 1){
                jumps++;
                return jumps;
            }
            if (i == endPtr){
                jumps++;
                endPtr = farthest;
            }
        }
        return jumps;
    }
};
