class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        arr ={}
        for i in range(len(nums)):
            if nums[i] not in arr:
                arr[nums[i]]=1
            else:
                return True
        return False
    
