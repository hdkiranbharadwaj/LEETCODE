class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # mx=0
        # i=0
        # while i < len(heights):
        #     count=1
        #     j=i
        #     while(j<len(heights)-1):
        #         if heights[j+1]>= heights[i]:
        #             count+=1
        #             j+=1
        #         else:
        #             break    
        #     j=i
        #     while j>=1 :
        #         if heights[j-1]>=heights[i]:
        #             count+=1
        #             j-=1
        #         else:
        #             break
        #     mx=max(mx,(count*heights[i])) 
        #     i+=1
        # return mx
        maxArea = 0
        stack = []  # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea
