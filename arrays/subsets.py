"""
Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
"""




class Solution:
    from itertools import combinations
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        for i in range(len(nums)+1):
            k=[ list(c) for c in combinations(nums,i)]
            for i in range(len(k)):
                result.append(k[i])
        return result
