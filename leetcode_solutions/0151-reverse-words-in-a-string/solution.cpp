class Solution {
public:
    string reverseWords(string s) {
        stringstream ss(s);
        string word;
        vector<string> words;
        while (ss >> word){
            words.push_back(word);
        }
        reverse(words.begin(), words.end());

        string returnString = "";
        for (int i = 0; i < words.size() - 1; i++){
            returnString += words[i] + " ";
        }

        return returnString + words[words.size() - 1];
    }
};
