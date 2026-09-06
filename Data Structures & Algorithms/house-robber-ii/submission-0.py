class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # solve hr1 for 0 to n-2
        # solve hr1 for 1 to n-1
        # return their max

        

        n = len(nums)
        if n < 3:
            return max(nums)
        dp = [0] * (n-1)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n-1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        ans1 = dp[-1]
        dp[0] = nums[1]
        dp[1] = max(nums[1], nums[2])
        for i in range(2, n-1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i+1])

        ans2 = dp[-1]
        return max(ans1, ans2)

