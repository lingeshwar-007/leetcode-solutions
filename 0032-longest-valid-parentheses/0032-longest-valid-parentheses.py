class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp=[0]*len(s)
        maxi=0
        for i in range(len(s)):
            if s[i]==')':
                prev=i-1
                if i>0 and dp[i-1]>0:
                    prev-=dp[i-1]
                if prev>=0 and s[prev]=='(':
                    dp[i]=i-prev+1
                if prev>0 and dp[i]>0 and dp[prev-1]>0:
                    dp[i]+=dp[prev-1]
                maxi=max(maxi,dp[i])
        return maxi