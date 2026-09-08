class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # dp[i] represents the min number of coins needed for that amount
        dp = [-1]* (amount+1)
        dp[0]=0

        for i in range(1, amount + 1):

            mincoins = float('inf')

            for coin in coins:
                if i - coin >= 0:
                    value = dp[i - coin] + 1

                    mincoins = min(value, mincoins)
            dp[i] = mincoins




        return -1 if dp[amount] == float("inf") else dp[amount]