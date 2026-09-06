class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ch = {}
        for x in s:
            if x in ch:
                ch[x]+= 1
            else:
                ch[x]=1
        for x in t:
            if x in ch:
                ch[x]-=1
                if ch[x] == 0:
                    del ch[x]
            else:
                return False

        return ch == {}
        