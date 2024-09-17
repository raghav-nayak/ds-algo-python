
Graphs are used to structure the problem
Algorithms are used to structure the problems
Algorithms are used to solve the problems.

Different solutions on Graphs
1. Connectivity - Paths/ relations / connections - e.g. MST -> Polynominal
2. Cyclicity - detecting cycles - e.g. TSP, dead-lock in resource accessing -> Non-polynominal
3. Colorability  -> Non-polynominal
4. Co-planarity  -> Non-polynominal


<hr>


## Question: why complete graph has time complexity of O(V^3)
The time complexity of **O(V³)** for operations on a **complete graph** typically arises when using algorithms that operate on all pairs of vertices, such as the **Floyd-Warshall algorithm** for finding the shortest paths between all pairs of vertices or algorithms that process all pairs of vertices (like some network flow algorithms). Here's why the time complexity is **O(V³)** in these cases:

### Complete Graph:

- A **complete graph** is a graph where every pair of distinct vertices is connected by a unique edge. This means that for a graph with **V** vertices, there are V(V−1)/2​ edges, but the key here is that each vertex is directly connected to every other vertex.

### Why O(V³)?

#### 1. **Iterating Over All Pairs of Vertices (O(V²))**:
- Many graph algorithms (like shortest path algorithms) involve iterating over **pairs of vertices**. In a graph with **V** vertices, the number of possible vertex pairs is V×V=V2V \times V = V²V×V=V2.
- For example, in the **Floyd-Warshall algorithm**, you need to iterate over every possible pair of vertices (i,j)(i, j)(i,j), which gives an initial time complexity of O(V2)O(V²)O(V2).
#### 2. **Processing Each Pair for Every Vertex (O(V))**:
- In some algorithms (such as Floyd-Warshall), for each pair of vertices, you process the information for every possible intermediate vertex **k**.
- This adds another loop over all vertices (i.e., checking paths through vertex **k** for each pair of **i** and **j**). Thus, you have three nested loops over **V** vertices, leading to a time complexity of **O(V³)**.
- The three loops are usually structured like this:
    - Outer loop: Iterates over every possible vertex **k**.
    - Middle loop: Iterates over every possible vertex **i** (starting vertex).
    - Inner loop: Iterates over every possible vertex **j** (ending vertex).

#### Example: Floyd-Warshall Algorithm
The Floyd-Warshall algorithm, which finds the shortest path between all pairs of vertices in a weighted graph, has three nested loops like this:

```Python
for k in range(V):
    for i in range(V):
        for j in range(V):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
```

- The **outer loop** iterates over all vertices **k**.
- The **two inner loops** iterate over all pairs of vertices **i** and **j**.
- This gives us **V * V * V = V³** iterations, resulting in **O(V³)** time complexity.

### Other Graph Algorithms with O(V³) Complexity:
1. **All-pairs shortest path** algorithms (like Floyd-Warshall).
2. Some versions of the **Maximum Flow** algorithms on dense graphs.
3. **Dynamic programming** solutions on graphs where you track paths through every vertex.

### Conclusion:
The **O(V³)** time complexity in complete graphs arises from algorithms that need to process **every possible pair of vertices** and possibly involve a third dimension (such as considering intermediate vertices). This is common in algorithms like Floyd-Warshall that solve the all-pairs shortest path problem by iterating over **every pair of vertices** and checking paths through **all other vertices**.


## Question: Other algorithm which are solved with < O(V^3) complexity

There are several algorithms that can potentially reduce the complexity for specific types of problems on graphs. While the **O(V³)** complexity is common for algorithms like **Floyd-Warshall** for all-pairs shortest paths on **dense graphs** (graphs where most pairs of vertices are connected), other algorithms can offer better time complexity, especially for **sparse graphs** (graphs with fewer edges relative to the number of vertices). Here are some key alternatives:

### 1. **Dijkstra’s Algorithm** (Single-Source Shortest Path)
- **Time Complexity**: O((V+E)log⁡V) using a priority queue.
- **Use Case**: This algorithm is used to find the shortest path from a **single source** to all other vertices. While Floyd-Warshall computes shortest paths for **all pairs**, Dijkstra’s algorithm works only for one source at a time.
- **Optimization**: If you only need shortest paths from a single source to all others (or a subset of all pairs), Dijkstra’s algorithm is more efficient for **sparse graphs** where the number of edges EEE is much smaller than V2V^2V2.
    You can run Dijkstra’s algorithm from every vertex if you need all-pairs shortest paths, which would give a time complexity of O(V(V+E) log⁡V), but this is better than **O(V³)** when EEE is much smaller than V^2.

### 2. **Johnson’s Algorithm** (All-Pairs Shortest Path)
- **Time Complexity**: O(V^2 log⁡V+VE).
- **Use Case**: Johnson’s algorithm is used for finding the shortest paths between all pairs of vertices. It works efficiently on **sparse graphs**.
- **How it Works**: It applies **Bellman-Ford** to handle negative weights and reweights the graph, followed by running **Dijkstra’s algorithm** for each vertex.
Since it uses Dijkstra's algorithm after reweighting, it has a better performance than Floyd-Warshall on graphs with fewer edges.

### 3. **Bellman-Ford Algorithm** (Single-Source Shortest Path with Negative Weights)
- **Time Complexity**: O(VE).
- **Use Case**: Bellman-Ford is used to find the shortest path from a single source to all vertices, even when the graph contains negative weight edges. It can handle cases where Dijkstra’s algorithm cannot, due to negative weights.
If you need all-pairs shortest paths, you can run Bellman-Ford from every vertex, which would result in a time complexity of **O(V²E)**. This is better than **O(V³)** when E ≪ V^2 

### 4. **A* Algorithm** (Single-Source Shortest Path with Heuristic)
- **Time Complexity**: In the worst case, it behaves like Dijkstra’s algorithm, O((V+E) log⁡V), but with a good heuristic, it can significantly reduce the number of explored nodes.
- **Use Case**: A* is commonly used in pathfinding problems where you want to find the shortest path between two specific nodes. It incorporates a heuristic to focus the search toward the goal, making it faster in many cases.

### 5. **Graph Sparsification** (For Dense Graphs)
- **Concept**: Graph sparsification is the process of approximating a dense graph by a sparse graph that approximately preserves properties like the shortest paths. Techniques like **spanners** and **cut sparsifiers** can be used to reduce the number of edges in dense graphs.
- **Use Case**: This is used when you have dense graphs and want to reduce the computational overhead by approximating it with a sparser graph, thus improving algorithm performance.

### 6. **Dynamic Shortest Path Algorithms**
- These algorithms are designed for graphs where the structure (e.g., edges or weights) is changing dynamically, and you want to maintain the shortest path efficiently without recalculating it from scratch every time.
- **Examples**: Dynamic variants of Dijkstra’s algorithm or Bellman-Ford, **Thorup’s Algorithm** for dynamic graph updates, and **Dynamic Tree** approaches.
- **Time Complexity**: These algorithms often aim to achieve sublinear or logarithmic time updates after changes in the graph.

### Summary:
- **For sparse graphs**: Algorithms like **Johnson’s** and **Dijkstra’s** with a priority queue offer better time complexity than **Floyd-Warshall**, especially if the number of edges EEE is much smaller than V2V²V2.
- **For dense graphs**: Floyd-Warshall remains efficient, but you can explore **graph sparsification** to reduce the number of edges, or use **heuristic-based algorithms** like A* if you are solving pathfinding problems.
- **For dynamic graphs**: Consider using **dynamic shortest path algorithms** to handle updates efficiently.

In conclusion, the best choice depends on the graph's characteristics (sparse vs. dense) and the specific problem (all-pairs shortest paths, single-source shortest paths, etc.). For many real-world applications, using Dijkstra’s algorithm or Johnson’s algorithm on sparse graphs provides significant improvements over the **O(V³)** complexity of Floyd-Warshall.