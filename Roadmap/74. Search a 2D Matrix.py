class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        lb=0
        ub=len(matrix)-1
        while lb<=ub:
            mid = (lb+ub)//2
            if matrix[mid][0]<=target<=matrix[mid][-1]:
                llb,uub=0,len(matrix[mid])-1
                while llb<=uub:
                    mmid=(llb+uub)//2
                    if matrix[mid][mmid] == target:
                        return True
                    elif target < matrix[mid][mmid]: 
                        uub=mmid-1
                    else:
                        llb=mmid+1
                return False
            elif target < matrix[mid][0]:
                ub=mid-1
            else:
                lb=mid+1
        return False


