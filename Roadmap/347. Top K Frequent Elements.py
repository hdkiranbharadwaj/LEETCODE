class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic={}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]]=1
            else:
                dic[nums[i]]+=1
        
        print(dic)
        sortedD = sorted(dic.items(), key=lambda x:x[1])[::-1]
        ret = []
        for i in range(k):
            ret.append(sortedD[i][0])
        print(sortedD)
        return ret
