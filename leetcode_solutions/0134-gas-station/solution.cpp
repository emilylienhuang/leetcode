class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int totalUsed = 0;
        int currentUsed = 0;
        int iStart = 0;
        for (int i = 0; i < gas.size(); i++){
            
            currentUsed += gas[i] - cost[i];
            totalUsed += gas[i] - cost[i];
        
            if (currentUsed < 0){
                iStart = i + 1;
                currentUsed = 0;
            }
        }
        return totalUsed >= 0 ? iStart : -1;
    }
};
