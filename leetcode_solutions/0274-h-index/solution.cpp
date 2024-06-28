class Solution {
public:
    int hIndex(vector<int>& citations) {
        sort(citations.begin(), citations.end(), greater<>());
        int n = citations.size();
        int h = 0;
        for (int i = 0; i < citations.size(); i++){
            if (citations[i] >= i + 1){
                // citations of paper >= number of papers cited before it x amount of times
                h++;
            }
        }

        return h;
    }
};
