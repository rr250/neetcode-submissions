class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if(len(prices) < 2):
        #     return 0
        # p=[0]
        # if(prices[1]>prices[0]):
        #     p.append(prices[1]-prices[0])
        # else:
        #     p.append(0)
        # for a in prices[2:]:
        #     print(a)

        # return p[-1]
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


    

        