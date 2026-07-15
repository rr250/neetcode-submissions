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
        print(i,tank)
        while(True):
            if i==maxIndex:
                return maxIndex
            tank=gas[i]-cost[i]+tank
            while tank<0:
                maxIndex=i
                tank=gas[i]-cost[i]
                if tank>=0:
                    break
                print('reset', i, tank)
                if i+1==len(gas):
                    i=0
                else:
                    i+=1
            if i+1==len(gas):
                i=0
            else:
                i+=1
            print(i,tank)
            
        return -1
        