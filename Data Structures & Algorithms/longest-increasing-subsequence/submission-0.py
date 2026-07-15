class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res=[0]
        def lis(last, size, i):
            if i==len(nums):
                res[0]=max(res[0], size)
                return
            lis(last, size, i+1)
            if last is None or last<nums[i]:
                lis(nums[i], size+1, i+1)
        lis(None, 0, 0)
        return res[0]

        