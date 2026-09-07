class Solution:
    def numDecodings(self, s: str) -> int:

        if s[0] == '0':
            return 0


        if len(s) <= 1:
            return len(s)

        

        

        # dp[i] represents the number of ways we can decode the string s[0:i+1]
        n = len(s)

        for i in range(1, n):
            if s[i] == '0' and s[i-1] not in '12':
                return 0 

        dp = [0] * n
        dp[0] = 1
        dp[1] = 2 if isPotentialTwoDigit(s[0:2]) else 1 

        
        for i in range(2, n):
            if isPotentialTwoDigit(s[i-1: i+1]):
                dp[i] = dp[i-2]  + dp[i-1]
            else:
                if s[i] != '0':
                    dp[i]= dp[i-1]
                else:
                    if isZeroValid(s[i-1: i+1]):
                        dp[i] = dp[i-2]
                    else:
                        return 0

        # print(dp, s)
        return dp[n-1]


def isZeroValid(s):
    return s[1] == '0' and s[0] in '12'
def isPotentialTwoDigit(s):
    return (s[0] == '1' and s[1] != '0') or (s[0] == '2' and (1 <= int(s[1])  <= 6))

