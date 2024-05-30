class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minPrice = prices[0];
        int maxProf = 0;
        for(auto &price: prices){
            if(price < minPrice){
                minPrice = price;
            } else if(price - minPrice > maxProf){
                maxProf = price - minPrice;
            }
        }
        return maxProf;
    }
};
