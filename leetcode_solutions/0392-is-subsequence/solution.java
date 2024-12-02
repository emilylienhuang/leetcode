class Solution {
    public boolean isSubsequence(String s, String t) {
        int pS = 0;
        int pT = 0;

        char[] sArray = s.toCharArray();
        char[] tArray = t.toCharArray();
        while (pS < s.length() && pT < t.length()){
            if (sArray[pS] == tArray[pT++]){
                pS++;
            }
        }
        return (pS == s.length()) ? true : false;
    }
}
