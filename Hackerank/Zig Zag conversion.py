"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);

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
--------------------------
#Logic
----------------------------
we need a zigzag like structure.For an example take HELLOWORLD ,RowSize=4
then,
H    O 
E  W R
L O  L
L    D
Add together,
HO + EWR + LOL + LD

We program it as:-
['H']   #In first round add words like this.(top-down)
['E']
['L']
['L']
--------
['HO']   #In second round,from down to up put words
['EW']
['LO']
['L']
--------
['HO']   #In third round,from up to down put words
['EWR']
['LOL']
['LD']
--------
#Now add all together = HO + EWR + LOL + LD
-----------------
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





        
