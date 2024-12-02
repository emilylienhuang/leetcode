class Solution {
public:
    bool isSubsequence(string s, string t) {
        int pS = 0;
        int pT = 0;
        while (pS < s.length() && pT < t.length()){
            if (s.at(pS) == t.at(pT++)){
                pS++;
            }
        }
        return pS == s.length() ? true : false;
    }
};
