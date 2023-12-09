class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        stack = []
        res =[]
        def backtrack(openN, closedN):
            print(stack)
            if openN==closedN==n:
                res.append(''.join(stack))
            if openN < n:
                stack.append('(')
                backtrack(openN+1,closedN)
                stack.pop()
            if closedN < openN:
                stack.append(')')
                backtrack(openN,closedN+1)
                stack.pop()
        backtrack(0,0)
        return res
