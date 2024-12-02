class Solution {
public:
    int romanToInt(string s) {
        map<char, int> romanNumerals = {{'I', 1}, {'V', 5},
                                            {'X', 10}, {'L', 50},
                                            {'C', 100}, {'D', 500},
                                            {'M', 1000}};
        int sum = 0;
        for (int i = 0; i < s.length(); i++){
            //loop through the string 
            char letter1 = s[i];
            char letter2 = s[i+1];
            int valueFirst = romanNumerals[letter1]; //number to be added or subtracted
            int valueSecond = romanNumerals[letter2];
            
            if (valueSecond > valueFirst){
                sum -= valueFirst;
            } else{
                sum += valueFirst;
            }
        }
        return sum;
    }
};
