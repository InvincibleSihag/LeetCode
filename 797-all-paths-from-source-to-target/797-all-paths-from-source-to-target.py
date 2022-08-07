class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        output = []
        def helper(source, path):
            # print(path)
            if source == len(graph)-1:
                output.append(list(path))
                return
            # print(graph[source])
            for node in graph[source]:
                path.append(node)
                helper(node, path)
                path.pop()
        helper(0, [0])
        return output
    