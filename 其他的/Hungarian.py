class HungarianAlgorithm:
    def __init__(self, graph):
        self.graph = graph
        self.left_size = len(graph)
        self.right_size = len(graph[0])
        self.matching = [-1] * self.left_size  # 存储最终的匹配方案

    def find_max_matching(self):
        for i in range(self.left_size):
            visited = [False] * self.left_size
            self._dfs(i, visited)

        max_matching = self.matching.count(-1)
        return max_matching, self.matching

    def _dfs(self, left_node, visited):
        for right_node in range(self.right_size):
            if self.graph[left_node][right_node] and not visited[left_node]:
                visited[left_node] = True

                if self.matching[right_node] == -1 or self._dfs(self.matching[right_node], visited):
                    self.matching[right_node] = left_node
                    return True

        return False

# 示例用法
graph = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 0, 1, 1]
]

hungarian = HungarianAlgorithm(graph)
max_matching, matching_result = hungarian.find_max_matching()

print("最大匹配数:", max_matching)
print("匹配方案:", matching_result)
