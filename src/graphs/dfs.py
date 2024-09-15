from collections import defaultdict

from src.graphs.graph import Graph


class DFS:
    def __init__(self) -> None:
        self._marked = defaultdict(bool)

    # Depth First Search
    # time complexity: O(Vertices X Edges)
    # total number of max possible edges in the graph : VC2 = V(V-1)/2!
    def dfs(self, graph: Graph, v: int) -> None:
        self._marked[v] = True
        for w in graph.get_adjacent_vertices(v):
            if not self._marked[w]:
                self.dfs(graph, w)


if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    dfs = DFS()
    dfs.dfs(g, 0)
    print(dfs._marked)
