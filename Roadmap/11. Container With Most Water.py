class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i=0
        j=len(height)-1
        count=0
        while i<j:
            res = (j-i)*min(height[i],height[j])
            count = max(count,res)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return count

        
