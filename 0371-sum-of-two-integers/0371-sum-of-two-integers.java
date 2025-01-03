class Solution {
    public int getSum(int a, int b) {
        // Use b as the carry
        // Use a as the sum
        while (b != 0){
            int tmp = (a & b) << 1; // calculate what will be carried over
            a = a ^ b; // performs addition w/o carrying
            b = tmp; // b stores the carry operation
        }
        return a;
    }
}