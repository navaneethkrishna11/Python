"""
Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21
"""
class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x<0
        x=abs(x)

        rev=0
        while x>0:
            rev=(rev*10)+x%10
            x=x//10
        
        if is_negative ==True:
            rev=-rev
        
        if rev<-2**31 or rev > 2**31-1:
            return 0
        return rev
        
