"""
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
 

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""







class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows ==1 or len(s)<=numRows:
            return s

        result = ['']  *numRows
        index = 0
        step = 1
        for char in s:
            result[index] += char
            if index == 0:
                step=1
            elif index == numRows-1:
                step= -1
            index += step
        
        return ''.join(result)





        
