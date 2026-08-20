class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0 ,1
        maxP = 0

        while r < len(prices):
            if prices[r] > prices[l]:
                val = prices[r] - prices[l]
                maxP = max(maxP, val)
            else:
                l = r
            r += 1
        return maxP

            

        #O(n): space
        #O(1): time: r scans each elements once l , move forward single pass
        
        
