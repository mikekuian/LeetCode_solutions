#A peak element is an element that is strictly greater than its neighbors.

#Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

#You may imagine that nums[-1] = nums[n] = -∞

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        def binarySearch(nums):
            """
            :type nums: List[int]
            :type target: int
            :rtype: int
            """
            if len(nums) == 0:
                return -1

            left, right = 0, len(nums) - 1
            while left < right:
                mid = (left + right) // 2
                if nums[mid] > nums[mid+1]:
                    right = mid
                
                else:
                    left = mid + 1

            return left
        
        return binarySearch(nums)

