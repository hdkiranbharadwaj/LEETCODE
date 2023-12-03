class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        lis=[]
        str
        for i in range(len(strs)):
            k = list(strs[i])
            k.sort()
            dic = {}
            for i in k:
                if(i not in dic):
                    dic[i]=1
                else:
                    dic[i]+=1
            p=""
            for i in dic:
                p=p+str(i)+str(dic[i])
            lis.append(p)
        print(lis)
        dic = {}
        for i in range(len(lis)):
            if lis[i] not in dic:
                d=[]
                dic[lis[i]]=d
                dic[lis[i]].append(str(strs[i]))
            else:
                dic[lis[i]].append(str(strs[i]))
        print(dic)
        lisy = []
        for i in dic:
            lisy.append(dic[i])
        return lisy
