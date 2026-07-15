class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj={}
        for f in flights:
            if f[0] in adj:
                adj[f[0]]+=[[f[1], f[2]]]
            else:
                adj[f[0]] = [[f[1], f[2]]]
        print(adj)
        minPrice = [99999999999999]
        def traverse(curr, k1, price):
            print(curr, k1, price)
            if curr == dst:
                minPrice[0]=min(minPrice[0],price)
                return
            if k1 == 0:
                return 
            if curr not in adj:
                return
            for a in adj[curr]:
                traverse(a[0], k1-1, price+a[1])
        traverse(src, k+1, 0)


        if minPrice[0] == 99999999999999:
            minPrice[0] = -1
        return minPrice[0]
        