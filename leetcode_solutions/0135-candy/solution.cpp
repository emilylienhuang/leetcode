class Solution {
public:
    int candy(vector<int>& ratings) {
        int n = ratings.size();
        vector<int> candies(n, 1);

        // Pass from left to right
        for (int i = 1; i < ratings.size(); i++){
            if (ratings[i-1] < ratings[i]){
                candies[i] = candies[i-1] + 1;
            }
        }

        // Pass from right to left
        for (int i = n - 2; i >= 0; i--){
            if (ratings[i+1] < ratings[i]){
                candies[i] = max(candies[i], candies[i+1] + 1);
            }
        }
        
        int returnSum = 0;
        for (auto & c: candies){
            returnSum += c;
        }
        return returnSum;
    }
};
