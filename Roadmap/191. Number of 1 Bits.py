class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        n=str(bin(n))
        k=0
        print(n)
        for i in range(len(n)):
            if n[i]=='1':
                k+=1
        return k
        
