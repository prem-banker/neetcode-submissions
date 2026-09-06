class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = {}
        postfix = {}
        curr = 1
        for i,el in enumerate(nums):
            if i == 0:
                prefix[i] = 1
            else:
                curr*=nums[i-1]
                prefix[i] = curr
        curr = 1
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums) - 1:
                postfix[i] = 1
            else:
                curr*=nums[i+1]
                postfix[i] = curr
        
        ans = []
        for i,el in enumerate(nums):
            ans.append(prefix[i] * postfix[i])
        return ans
