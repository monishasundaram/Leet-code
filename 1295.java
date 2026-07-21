class Solution {
    public int findNumbers(int[] nums) {
        int c = 0;
        for (int i = 0; i<nums.length ; i++){
           int a = 0;
           int b = nums[i];
           while(b>0){
            b/=10;
            a = a+1;
           }
           if(a%2==0){
            c += 1;
           }
        }
        return c;
    }
}
