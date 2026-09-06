class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanum = 'abcdefghijklmnopqrstubwxyz1234567890'
        ns = ''
        for ch in s.lower():
            if ch in alphanum:
                ns+=ch
        return ns == ns[::-1]