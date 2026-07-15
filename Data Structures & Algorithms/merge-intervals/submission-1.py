class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if(len(intervals)==0):
            return []
        A = sorted(intervals)
        l,r=A[0]
        res=[]
        for a in A:
            if a[0]>r:
                res.append([l,r])
                l,r=a
            else:
                r=max(r, a[1])
        res.append([l,r])
        return res


                
