class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def allPathsHelper(sv,ev,graph,output,ans):
            if sv == ev:
                output.append(ans)

            for i in graph[sv]:
                allPathsHelper(i,ev,graph,output,ans + [i])
            return output

        def allPaths(graph):
            sv = 0
            ev = len(graph)-1
            ans = allPathsHelper(sv,ev,graph,[],[sv])
            return ans
        return allPaths(graph)
        