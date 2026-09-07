class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) <= 1:
            return 1
    
        n = len(s)
        dp = [[False]*n for i in range(n)]

        ans = 0
        ansString = ''
       
        for i in range(n, -1, -1):
            for j in range(i, n):
         
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

                if dp[i][j]:
                    ans+=1
         
        return ans