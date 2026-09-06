class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i,j= 0, n-1
        maxval = 0
        while(i<j):
            maxval = max(maxval, (j-i) * min(heights[i] , heights[j]))
            if heights[i] < heights[j]:
                i+=1
            elif heights[i] > heights[j]:
                j-=1
            else:
                i+=1
                j-=1
        return maxval