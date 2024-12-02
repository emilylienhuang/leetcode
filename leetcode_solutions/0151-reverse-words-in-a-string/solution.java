class Solution {
    public String reverseWords(String s) {
        String[] words = s.trim().split("\\s+");

        String output = "";

        for (int i = words.length - 1; i > 0; i--){
            output += words[i] + " ";
        }

        return output + words[0];

       
            
    }
}
