class Solution {
    public int maxProfit(int[] prices) {
        int max=0;
        int i=1,j=0;
        while(i<prices.length)
        {
            if(prices[j]<prices[i])
            {
                max=Math.max(prices[i]-prices[j],max);
            }
            else 
             j=i;
             i++;
        }
        
        return max;
    }
}
