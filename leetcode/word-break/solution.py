
class Solution(object):
    def wordBreak(self, s, wordDict):
       slen=len(s)
       wordset=set(wordDict)
       dp=[False]*(slen+1)
       dp[0]=True

       for i in range(1,slen+1):
        for j in range(i):
            if dp[j] and s[j:i] in wordset:
                dp[i]=True
                break
       return dp[slen]


        
        