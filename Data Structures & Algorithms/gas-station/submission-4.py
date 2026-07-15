class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        maxDiff = [x1 - x2 for (x1, x2) in zip(gas, cost)]
        maxValue = max(maxDiff)
        maxIndex = maxDiff.index(maxValue)
        i=maxIndex
        if i+1==len(gas):
            i=0
        else:
            i+=1
        tank=maxValue
        while(True):
            if i==maxIndex:
                return maxIndex
            tank=gas[i]-cost[i]+tank
            if tank<0:
                maxIndex=i
                tank=gas[i]-cost[i]
            if i+1==len(gas):
                i=0
            else:
                i+=1
            
        return -1
        