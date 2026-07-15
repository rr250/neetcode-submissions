class Solution:
    def trap(self, height: List[int]) -> int:
        l=[0]
        r=[0]
        lmax,rmax=0,0
        for i in range(1, len(height)):
            lmax = max(lmax, height[i-1])
            l.append(lmax)
        for i in range(len(height)-2,-1,-1):
            rmax = max(rmax, height[i+1])
            r.append(rmax)
        r.reverse()
        res=0
        for i in range(len(height)):
            res+=max(min(l[i],r[i])-height[i],0)
        return res
        
        