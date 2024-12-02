class Solution {
    public String convert(String s, int numRows) {
        if (numRows == 1){
            return s;
        }
        String[] rows = new String[numRows];
        Arrays.fill(rows, "");
        int dir = 1;
        int iRow = 0;
        for (int iString = 0; iString < s.length(); iString++){
            rows[iRow] += s.charAt(iString);
            iRow += dir;
            if (iRow == 0 || iRow == numRows - 1){
                dir = -dir;
            }
        }
        String retStr = "";
        for (String row: rows){
            retStr += row;
        }

        return retStr;
    }
}
