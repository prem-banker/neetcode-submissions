class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        for s in strs:
            x = ''.join(sorted(list(s)))
            if x in words:
                words[x].append(s)
            else:
                words[x]=[s]

        ans = []
        for el in words:
            ans.append(words[el])
        return ans
