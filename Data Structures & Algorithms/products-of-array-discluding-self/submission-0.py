class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ps = [[1,1] for _ in range(len(nums))]
        
        for i, n in enumerate(nums[1:]):
            print(i+1, n, ps, ps[i][0], nums[i],ps[i+1][1])
            ps[i+1] = ps[i][0]*nums[i], ps[i+1][1]
        for j, n in enumerate(list(reversed(nums))[1:]):
            i=len(nums)-1-j
            print(i-1, n, ps, ps[i][0], nums[i],ps[i-1][1])
            ps[i-1] = ps[i-1][0], ps[i][1]*nums[i]
        print(ps)
        res=[]
        for a in ps:
            res.append(a[0]*a[1])

        return res

        