class TimeMap(object):

    def __init__(self):
        self.has = {}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.has:
            self.has[key]=[]
        self.has[key].append([value,timestamp])
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        # if key not in self.has:
        #     return ""
        # #     timestamps = list(self.has[key].keys())
        
        #     for i in sorted(timestamps)[::-1]:
        #         if i<=timestamp:
        #             return self.has[key][i]
        # return ""
        # lis = (list(self.has[key].keys()))
        # l,r = 0,len(lis)-1
        # closest=-1
        # while l<=r:
        #     mid=(l+r)//2
        #     if lis[mid]<=timestamp:
        #         closest = lis[mid]
        #         l=mid+1
        #     else:
        #         r=mid-1
        # if closest == -1:
        #     return ""
        # return self.has[key][closest]
        res=""
        values = self.has.get(key,[])
        l,r=0,len(values)-1
        while l<=r:
            m=(l+r)//2
            if values[m][1]<=timestamp:
                res = values[m][0]
                l=m+1
            else:
                r=m-1
        return res
        
        
            
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)