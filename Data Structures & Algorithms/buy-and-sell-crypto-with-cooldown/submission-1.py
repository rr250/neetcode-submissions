class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit=[0]
        def profit(i, haveCoin, currProfit):
            maxProfit[0]=max(maxProfit[0], currProfit)
            if i>=len(prices):
                return
            if haveCoin:
                profit(i+2, False, currProfit+prices[i])
                profit(i+1, True, currProfit)
            else:
                profit(i+1, False, currProfit)
                profit(i+1, True, currProfit-prices[i])
        
        profit(0, False, 0)
        return maxProfit[0]


    

        