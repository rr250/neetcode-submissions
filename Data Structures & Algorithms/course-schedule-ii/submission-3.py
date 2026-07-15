class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj={}
        visited=[0]*numCourses
        for i in range(numCourses):
            adj[i]=set([])
        for l in prerequisites:
            adj[l[1]].add(l[0])
        print(adj)
        res=[]
        def traverse(curr):
            # print(visited)
            visited[curr]=1
            # res.append(curr)
            for b in adj[curr]:
                if visited[b]==1:
                    return False
                elif visited[b]==0:
                    if not traverse(b):
                        return False
            res.append(curr)
            visited[curr]=2
            return True
        
        # for i in range(numCourses):
        #     if len(adj[i])==0:
        #         visited.add(i)


        for i in range(numCourses):
            if visited[i]==0:
                if not traverse(i):
                    # print(visited)
                    return []
        res.reverse()

            
        return res

    
        