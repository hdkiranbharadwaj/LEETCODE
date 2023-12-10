class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        
        
        lb, ub= 1, max(piles)
        res=ub
        while lb<=ub:
            mid = (lb+ub)//2
            hours = 0
            for p in piles:
                hours+=math.ceil(float(p)/mid)
            if hours<=h:
                res=min(res,mid)
                ub=mid-1
            else:
                lb=mid+1
        return res



        
