class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int startingStation = 0;
        int currGas = 0;
        int totalGas = 0;
        for (int i = 0; i < gas.size(); i++){
            totalGas += gas[i] - cost[i];
            currGas += gas[i] - cost[i];
            if (currGas < 0){
                startingStation = i+1;
                currGas = 0;
            }
        }
        return totalGas >= 0 ? startingStation : -1;
    }
};
