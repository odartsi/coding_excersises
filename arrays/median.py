'''
Description:
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
---

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.


Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

wikipedia link: https://en.wikipedia.org/wiki/Median
'''


class Solution:
    
    def calculate_median(self,x,n):
        if n%2 !=0:
            return x[int((n+1)/2 -1)]
        else:
            return (x[int(n/2 -1)] + x[int(n/2)])/2
            
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3=sorted(nums1+nums2)
        
        median = self.calculate_median(nums3,len(nums3))
        
        return median
