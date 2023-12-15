class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        
        low = 0
        high = len(nums) - 1
        mid = low+high/2
        
        if nums[high] > nums[low]:
            return nums[0]
        
        while low<high:
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            elif nums[mid-1]>nums[mid]:
                return nums[mid]
            elif nums[mid] > nums[low]:
                low=mid+1
            else:
                high=mid-1
            mid=(low+high)/2
