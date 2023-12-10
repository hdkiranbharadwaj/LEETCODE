def eval(a,b,op):
    if op=='+':
        return (a)+(b)
    elif op=='*':
        return (a)*(b)
    elif op=='/':
        return  a//b if a*b >= 0 else -(-a//b)
    elif op=='-':
        return (a)-(b)

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack=[]
        oper=['*','+','-','/']
        for i in range(len(tokens)):
            if tokens[i] not in oper:
                stack.append(int(tokens[i]))
            else:
                b=stack.pop()
                a=stack.pop()
                sol=(eval(a,b,tokens[i]))
                stack.append(sol)
        return int(stack[-1])
