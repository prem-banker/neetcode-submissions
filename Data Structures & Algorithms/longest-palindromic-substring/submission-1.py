class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # prem12345321mer

        # dp 2d array where dp[i][j] suggest that s from inded i tp j is palindromic
        # True if   dp[i][j] is True and all are same

        if len(s) <= 1:
            return s
    
        n = len(s)
        dp = [[False]*n for i in range(n)]

        ans = 1
        ansString = ''
       
        for i in range(n, -1, -1):
            for j in range(i, n):
                # if (i == 1 and j == 4):
                #     print("dp bef", dp)
                # represents negative or zero length
                if i > j :
                    continue

                # reps single character
                if (j - i) == 0:
                    dp[i][j] = True                
                
                # matching first and last
                elif (j - i) <= 2:
                    dp[i][j] = (s[i] == s[j])

                # size >= 4
                else:
                        dp[i][j] = dp[i+1][j-1] and (s[i] == s[j])

                if dp[i][j] and (j-i+1) >= ans:
                    ans = j-i+1
                    ansString = s[i:j+1]
                # if (i == 1 and j == 4):
                #     print("dp aft", dp)
        return ansString


