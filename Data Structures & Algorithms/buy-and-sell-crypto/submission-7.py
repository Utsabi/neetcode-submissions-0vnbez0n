class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0,1
        trans=0

        while j < len(prices):
            if prices[i]<prices[j]:
                trans=max(trans,prices[j]-prices[i])
                j+=1                
            else:               
                i=j
                j=j+1
                
        return trans

        