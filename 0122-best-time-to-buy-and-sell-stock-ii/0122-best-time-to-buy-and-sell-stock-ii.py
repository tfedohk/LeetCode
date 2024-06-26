class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # print("prices: {}".format(prices))
        minimum_price = prices[0]
        candidates= []
        
        for idx, price in enumerate(prices):
            if price >= minimum_price:
                candidates.append(price - minimum_price)
                
            minimum_price = price
            
        # print("candidates: {}".format(candidates))
        return sum(candidates)