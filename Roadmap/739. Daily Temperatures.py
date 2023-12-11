class Solution(object):
    def dailyTemperatures(self, t):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        res = [0]*len(t)
        stack = [] 
        for i,te in enumerate(t):
            while stack and te > stack[-1][0]:
                temp, index = stack.pop()
                res[index]=(i-index)
            stack.append([te,i])
        return res
