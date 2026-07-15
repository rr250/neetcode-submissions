class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # for a in intervals:

        #     for r in res:
        #         if a[0]<r[0]:
        #             print(a, r)
        #         if a[0]>=r[0] and a[0]<=r[1]:
        #             print(a, r)
        #         if a[0]>r[1]:
        #             print(a, r)

        #         if a[1]<r[0]:
        #             print(a, r)
        #         if a[1]>=r[0] and a[1]<=r[1]:
        #             print(a, r)
        #         if a[1]>r[1]:
        #             print(a, r)
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


                
