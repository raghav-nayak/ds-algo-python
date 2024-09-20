from collections import defaultdict, deque

from src.graphs.graph import Graph


class BFS:
    def __init__(self, graph: Graph, source: int) -> None:
        self._graph = graph
        self._source = source
        self._marked = defaultdict(bool)
        self._bfs(s=self._source)

    def _bfs(self, s: int) -> None:
        self._marked[s] = True
        queue = deque()
        queue.append(s)
        while len(queue) > 0:
            v = queue.popleft()
            for w in self._graph.get_adjacent_vertices(v):
                if not self._marked[w]:
                    self._marked[w] = True
                    queue.append(w)


if __name__ == "__main__":
    g = Graph(7)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 5)
    g.add_edge(0, 6)
    g.add_edge(5, 4)
    g.add_edge(4, 6)
    g.add_edge(6, 0)

    bfs_graph = BFS(graph=g, source=0)
    print(bfs_graph._marked)
