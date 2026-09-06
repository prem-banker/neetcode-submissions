class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        for i, el in enumerate(nums):
            
            if (i > 0 and nums[i] != nums[i-1] and nums[i] <= 0) or (i == 0 and nums[i] <= 0 ):
                j, k = i+1, n-1
                while(j < k):
                    target = nums[i] + nums[j] + nums[k]
                    if target > 0:
                        k-=1
                    elif target < 0:
                        j+=1
                    else:
                        ans.append([nums[i], nums[j], nums[k]])
                        j+=1
                        k-=1
                        while nums[j] == nums[j - 1] and j < k:
                            j += 1
        return ans



                