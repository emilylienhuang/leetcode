class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int starting_station = 0;
        int prev_gas = 0;
        int curr_gas = 0;
        for (int i = 0; i < gas.size(); i++){
            curr_gas += gas[i] - cost[i];
            if (curr_gas < 0){
                prev_gas += curr_gas;
                curr_gas = 0;
                starting_station = i+1;
            }
        }
        return (prev_gas + curr_gas) >= 0 ? starting_station : -1;
    }
};
