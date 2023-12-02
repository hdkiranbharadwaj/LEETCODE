class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lis = [1]*len(nums)
        for i in range(1,len(nums)):
            lis[i]=lis[i-1]*nums[i-1]
        print(lis)
        k=nums[len(nums)-1]
        for i in (range(0,len(nums)-1)[::-1]):
            lis[i]=lis[i]*k
            k=k*nums[i]
        return lis
#################################################################

#################################################################
def leftpr(nums, index, leftp):
        if leftp[index] != 'a' :
            return leftp[index]
        elif index==0 :
            leftp[index]=1
        else:
            leftp[index]*=leftpr(nums,index-1,leftp)
        return leftp[index]
    
def rleftpr(nums, index, rleftp):
        print(rleftp)
        if rleftp[index] != 'a' :
            return rleftp[index]
        elif index==(len(nums)-1):
            rleftp[index]=1
        else:
            rleftp[index]*=rleftpr(nums,index+1,rleftp)
        return rleftp[index]


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        leftp=['a']*len(nums)
        rleftp=['a']*len(nums)
        ret = []
        for i in range(len(nums)):
            ret.append(leftpr(nums,i,leftp)*rleftpr(nums,i,leftp))

