class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        i,j=0,0
        dp=[]
        res=[]
        while(i<len(t)):
            while(j<len(t) and t[i]>=t[j]):
                print(i,j,t[i],t[j])
                j+=1
            if(j<len(t) and t[i]<t[j]):
                print(i,j,t[i],t[j])
                res.append(j-i)
            else:
                print(i,j,t[i])
                res.append(0)
            dp.append(j)
            i+=1
            j=i
        return res
        