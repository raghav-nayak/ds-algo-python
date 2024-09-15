from collections import defaultdict

from src.graphs.graph import Graph


class DFSPaths:
    def __init__(self, graph: Graph, source: int) -> None:
        self._graph = graph
        self._source = source
        self._marked = defaultdict(bool)
        self._edge_to = [None] * self._graph.get_vertices()

        # initialize graph with source
        self._edge_to[source] = source  # pre-processing
        self._dfs(graph, self._source)

    def _dfs(self, graph: Graph, s: int):
        self._marked[s] = True
        for w in graph.get_adjacent_vertices(s):
            if not self._marked[w]:
                self._edge_to[w] = s
                self._dfs(graph, w)

    def path_to(self, v: int) -> list:
        stack = list()
        i = v
        while i != self._source:
            stack.append(i)
            i = self._edge_to[i]
        stack.append(self._source)
        return stack


if __name__ == "__main__":
    g = Graph(7)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 5)
    g.add_edge(0, 6)
    g.add_edge(5, 4)
    g.add_edge(4, 6)
    g.add_edge(6, 0)

    dfs_paths = DFSPaths(graph=g, source=0)
    print(dfs_paths.path_to(4))
