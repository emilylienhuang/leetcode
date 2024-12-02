class Solution {
public:
    int majorityElement(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        
        int times = nums.size()/ 2;
        map<int, int> m;
        for (auto &n : nums){
            if (m.find(n) == m.end()){
                m[n] = 1;
            }else{
                m[n] += 1;
            }
            if (m[n] > times){
                return n;
            }
        }
        
        return m[times];
    }
};
