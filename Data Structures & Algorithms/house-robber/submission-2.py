class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return max(nums)
        
        # dp[i] represents the max ammount received till house number i

        dp = [-1] * n
        dp[0] = nums[0]
        dp[1] = nums[1]
        for i in range(2, n):
            # either take it or leave it
            dp[i] = max(dp[i-1], nums[i] + dp[i-2], nums[i] + dp[i-3])

        return dp[n-1]
