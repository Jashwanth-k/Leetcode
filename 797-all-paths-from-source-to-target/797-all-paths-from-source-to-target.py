class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def allPathsHelper(sv,ev,graph,output,ans):
            if sv == ev:
                output.append(ans)
                return

            for i in graph[sv]:
                allPathsHelper(i,ev,graph,output,ans + [i])
            return output

        sv = 0
        ev = len(graph)-1
        return allPathsHelper(sv,ev,graph,[],[sv])
        