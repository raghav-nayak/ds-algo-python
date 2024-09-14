from collections import defaultdict


class Graph:
    def __init__(self, vertices: int) -> None:
        self._vertices = vertices
        self._edges: int = 0
        self._graph = defaultdict(list)

    def add_edge(self, v: int, w: int) -> None:
        self._graph[v].append(w)
        self._graph[w].append(v)
        self._edges += 1

    def get_vertices(self) -> int:
        return self._vertices

    def get_edges(self) -> int:
        return self._edges

    def get_adjacent_vertices(self, v: int) -> list[int]:
        return self._graph[v]


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