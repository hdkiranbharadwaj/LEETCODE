class Solution(object):
   
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        cset = set()
        l=0
        res=0
        for r in range(len(s)):
            while s[r] in cset:
                cset.remove(s[l])
                l+=1
            cset.add(s[r])
            res=max(res,r-l+1)
        return res

        
