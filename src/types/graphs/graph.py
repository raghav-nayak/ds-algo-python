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
