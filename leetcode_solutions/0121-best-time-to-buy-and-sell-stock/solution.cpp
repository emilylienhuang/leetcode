class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minPrice = prices[0];
        int maxProf = 0;
        for (int price: prices){
            if (price < minPrice){
                minPrice = price;
            } else if (price > minPrice){
                maxProf = max(price - minPrice, maxProf);
            }
        }
        return maxProf;
    }
};
