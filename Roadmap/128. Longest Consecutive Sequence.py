class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for i in range(len(nums)):
                dic[nums[i]]=1
           
        K=0
        k=0

        for i in dic:
            if i-1 not in dic:
                k=1
                current_ele=i
                while current_ele+1 in dic:
                    k=k+1
                    current_ele=current_ele+1
                    
                if K<k:
                    K=k
                    o=0
                         
        return K
        
