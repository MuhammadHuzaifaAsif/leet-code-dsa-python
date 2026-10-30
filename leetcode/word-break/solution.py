       for i in range(1,slen+1):
        for j in range(i):
            if dp[j] and s[j:i] in wordset:
                dp[i]=True
       dp[0]=True

                break
       return dp[slen]


        
        
