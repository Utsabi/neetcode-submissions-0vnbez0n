class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0,1
        trans=0

        while j < len(prices):
            if prices[i]<prices[j]:
                maxi = prices[j]-prices[i]
                trans=max(trans,maxi)               
            else:               
                i=j          
            j=j+1   
        return trans

        