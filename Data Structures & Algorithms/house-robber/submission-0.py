class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n< 3:
            return max(nums)
        
        maxm = [0] * n
        maxm[0] = nums[0]
        maxm[1] = max(nums[0], nums[1])

        for i in range(2,n):
            maxm[i] = max(maxm[i-2] + nums[i], maxm[i-1])
        
        return maxm[-1]