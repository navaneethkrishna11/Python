"""
Longest palindrome substring of a string using Dynamic programming..
"""
def long(s):
    n=len(s)
    dp= [[False]*n for _ in range(n)]
    max_length = 1
    start=0

    for i in range(n):
         dp[i][i]=True

    for i in range(n-1):
          if s[i] ==s[i+1]:
               dp[i][i+1]=True
               start=1
               max_length=2


    for length in range(3,n-1):
         for i in range(n - length + 1):
             j= i + length-1
             if s[i]==s[j] and dp[i+1][j-1]:
                  dp[i][j]=True
                  if length>max_length:
                         start=i
                         max_length=length

    return s[start :start + max_length]

print(long("abcbedrardea"))

