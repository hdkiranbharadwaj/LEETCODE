class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # min(max(left),max(right)) - h[i] (height at that position)
        # ml=[0]*len(height)
        # mr=[0]*len(height)
        
        # for i in range(1,len(height)):
        #     ml[i]=max(height[i-1],ml[i-1])
        #     k=len(height)-i-1
        #     mr[k]=max(height[k+1],mr[k+1])
        # count =0
        # for i in range(len(height)):
        #     count+= 0 if (min(ml[i],mr[i])-height[i]) < 0 else ( min(ml[i],mr[i])-height[i] )
        # return count
        if not height : return 0
        l,r = 0, len(height)-1
        leftMax,rightMax = height[l],height[r]
        count=0
        while(l<r):
            if leftMax < rightMax:
                l+=1
                leftMax=max(leftMax,height[l])
                count+=leftMax - height[l]
            else:
                r-=1
                rightMax=max(rightMax,height[r])
                count+=rightMax - height[r]
        return count
