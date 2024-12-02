class Solution {
    public int trap(int[] height) {
        int rPtr = 0;
        int lPtr = height.length - 1;

        int rMax = height[rPtr];
        int lMax = height[lPtr];

        int totalWater = 0;
        while (rPtr < lPtr){
            if (height[rPtr] < height[lPtr]){
                if (height[rPtr] >= rMax){
                    rMax = height[rPtr];
                } else {
                    totalWater += rMax - height[rPtr];
                }
                rPtr++;
            } else {
                if (height[lPtr] >= lMax){
                    lMax = height[lPtr];
                } else {
                    totalWater += lMax - height[lPtr];
                }
                lPtr--;
            }
        }
        return totalWater;
    }
}
