class Solution:
    def power(self,x,y,p):  
        res = 1     
        x = x % p   
        if x == 0: 
            return 0 
        while y > 0:
            if y % 2==1:   
                res = (res*x) % p  
            y = y>>1 
            x = (x*x) % p  
        return res  
    def kvowelwords(self, N,K):
        MOD = 1000000007
        dp=[[0 for j in range(K+1)] for i in range(N+1)]
        sum=1
        for i in range(1,N+1):
            dp[i][0]=sum*21
            dp[i][0]%=MOD
            sum=dp[i][0]
            for j in range(1,K+1):
                if j>i:
                    dp[i][j]=0
                elif j==i:
                    dp[i][j]=self.power(5,i,MOD)
                else:
                    dp[i][j]=dp[i-1][j-1]*5
                dp[i][j]%=MOD
                sum+=dp[i][j]
                sum%=MOD
        return sum
