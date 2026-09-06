class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = {}
        for i,num in enumerate(nums):
            if target - num in x:
                return [x[target - num], i]
            else:
                x[num] = i