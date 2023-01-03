"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
"""

class Solution(object):
    def generate(self,numRows):

        output=[[]]*numRows
        output[0]=[1]
        for i in range(1,numRows):
        
            output[i]=[output[i-1][j] + output[i-1][j+1] for j in range(len(output[i-1])-1)]
            output[i].append(1)
            output[i].insert(0,1)
        return output[:numRows]
