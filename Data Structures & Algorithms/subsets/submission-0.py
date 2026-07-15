class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        def subset(A):
            nonlocal res
            print(res)
            if(A not in res):
                res.append(A)
            if(len(A)==1):
                return
            for i in range(len(A)):
                a=A[:i]+A[i+1:]
                subset(a)
        subset(nums)
        # print(nums[1:2])
        return res