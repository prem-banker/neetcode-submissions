class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <=1:
            return len(s)
        curr = s[0]
        maxval = 1
        for i, el in enumerate(s[1:], 1):
            loc = curr.find(el)
            if loc != -1:
                curr=curr[loc+1: ]
            curr+=el
            maxval = max(len(curr), maxval)

        return maxval


        