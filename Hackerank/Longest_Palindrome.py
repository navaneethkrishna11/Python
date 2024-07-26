"""
Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        start=0
        end=0
        
        for i in range(len(s)):
            len1 = expandAroundCenters(s,i, i)
            len2 = expandAroundCenters(s,i,i+1)
             
            length=max(len1,len2)
            if length > end - start :
                start =i-(length-1)//2
                end=i+length//2
        
        return s[start:end+1]
 
    
def expandAroundCenters(s,left,right):
    while left>=0 and right< len(s) and s[left]==s[right]:
        left -= 1
        right += 1
    
    return right-left-1
    
 
 



                
        
            
        
