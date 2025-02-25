Here's the **final enhanced table** with the following details for each algorithm:
- **Graph Type**: Directed or Undirected  
- **Cyclic/Acyclic Support**: Whether it works on cyclic, acyclic, or both  
- **Failure Cases**: Where the algorithm fails and why  

---

### 📊 **Graph Algorithms, Graph Types, Cyclic Support, and Failure Cases**

| **Algorithm**                    | **Graph Type**           | **Cyclic/Acyclic**      | **Purpose**                            | **Fails On**                                      | **Reason for Failure**                                                                                   |
|----------------------------------|--------------------------|-------------------------|----------------------------------------|--------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| **BFS (Breadth-First Search)**   | Both                     | Both                    | Shortest path in unweighted graphs     | Weighted graphs                                  | Ignores edge weights, leading to incorrect shortest paths.                                             |
| **DFS (Depth-First Search)**     | Both                     | Both                    | Connectivity, cycle detection          | Large/deep graphs (stack overflow)               | Recursion limit exceeded in large/deep graphs.                                                          |
| **Dijkstra's Algorithm**         | Both                     | Both                    | Shortest path in weighted graphs       | Graphs with negative weight edges                | Cannot handle negative weights, giving incorrect paths.                                                |
| **Bellman-Ford Algorithm**       | Directed (Undirected with modifications) | Both | Shortest path (handles negatives)      | Graphs with negative weight cycles               | Fails due to infinite distance reductions in negative cycles.                                          |
| **Floyd-Warshall Algorithm**     | Both                     | Both                    | All-pairs shortest paths               | Graphs with negative weight cycles               | Incorrect distances due to infinite loops in negative cycles.                                          |
| **Prim's Algorithm**             | Undirected               | Both                    | Minimum Spanning Tree (MST)            | Directed graphs                                  | MST isn't defined for directed graphs.                                                                 |
| **Kruskal's Algorithm**          | Undirected               | Both                    | Minimum Spanning Tree (MST)            | Directed graphs, disconnected graphs             | Fails on directed graphs; can't form MST if disconnected.                                              |
| **Topological Sort (DFS-based)** | Directed (DAG only)      | **Acyclic only**        | Task scheduling, dependency resolution | Graphs with cycles                               | Topological sorting not possible in cyclic graphs.                                                     |
| **Tarjan's Algorithm (SCC)**     | Directed                 | Both                    | Strongly Connected Components (SCC)    | None (robust)                                    | Correct for all directed graphs.                                                                       |
| **Kosaraju's Algorithm**         | Directed                 | Both                    | Strongly Connected Components (SCC)    | None (robust)                                    | Efficient for all directed graphs.                                                                     |
| **Union-Find (Disjoint Set)**    | Undirected (Directed with modifications) | Both | Cycle detection, MST (Kruskal)         | Directed graphs (without modifications)          | Requires changes for directed graphs.                                                                  |
| **A* Search Algorithm**          | Both                     | Both                    | Optimal pathfinding                    | Heuristic overestimates cost                     | Produces suboptimal paths if heuristic isn't admissible.                                               |
| **Johnson's Algorithm**          | Directed                 | Both                    | All-pairs shortest paths               | Graphs with negative weight cycles               | Fails if negative weight cycles exist.                                                                 |
| **Edmonds-Karp Algorithm**       | Directed                 | Both                    | Maximum Flow (Ford-Fulkerson variant)  | Graphs with irrational capacities               | Poor convergence with irrational capacities due to infinite precision issues.                           |
| **Ford-Fulkerson Algorithm**     | Directed                 | Both                    | Maximum Flow                           | Graphs with irrational capacities               | May not converge to the correct solution.                                                              |
| **Hopcroft-Karp Algorithm**      | Undirected (Bipartite)   | Both                    | Maximum matching in bipartite graphs   | Non-bipartite graphs                             | Designed only for bipartite graphs.                                                                    |
| **Hierholzer’s Algorithm**       | Both                     | **Cyclic preferred**    | Finding Eulerian Path/Circuit          | Graphs without Eulerian conditions              | Requires specific degree conditions (cyclic properties).                                              |
| **Warshall’s Algorithm**         | Directed                 | Both                    | Transitive closure                     | None (robust)                                    | Correct for all directed graphs.                                                                       |
| **Kahn’s Algorithm**             | Directed (DAG only)      | **Acyclic only**        | Topological sorting                    | Graphs with cycles                               | Only works on acyclic graphs (DAGs).                                                                   |
| **Bridges & Articulation Points (Tarjan's)** | Undirected | Both | Critical connections/nodes              | None (robust)                                    | Correct for all undirected graphs.                                                                    |
| **PageRank Algorithm**           | Directed (Web Graphs)    | Both                    | Node ranking (e.g., web pages)         | Small, disconnected graphs                      | Results are less meaningful for small or disconnected graphs.                                          |
| **Dinic's Algorithm**            | Directed                 | Both                    | Maximum Flow                           | Dense graphs                                    | Performance degrades on dense graphs.                                                                 |
| **Johnson-Trotter Algorithm**    | N/A (Permutation Algo)   | N/A                     | Generating permutations               | N/A                                             | Not a graph algorithm.                                                                                |
| **Boruvka's Algorithm**          | Undirected               | Both                    | Minimum Spanning Tree                  | Directed graphs                                 | Not designed for directed graphs.                                                                     |
| **Gabow's Algorithm**            | Directed                 | Both                    | Strongly Connected Components (SCC)    | None (robust)                                    | Works efficiently on all directed graphs.                                                             |

---

### 🚩 **Key Insights:**

1. **Cyclic vs Acyclic Sensitivity:**
   - **Fails on Cyclic Graphs:**  
     - **Topological Sort** and **Kahn’s Algorithm** are strictly for **acyclic** graphs (DAGs).  
   - **Requires Cycles:**  
     - **Hierholzer’s Algorithm** works best when cycles exist (Eulerian paths/circuits).  

2. **Negative Cycles:**
   - Algorithms like **Bellman-Ford**, **Johnson’s**, and **Floyd-Warshall** fail in the presence of **negative weight cycles**.  

3. **Directed vs Undirected:**
   - MST algorithms like **Prim’s**, **Kruskal’s**, and **Boruvka’s** are designed for **undirected graphs**.  
   - Algorithms for **strongly connected components (SCC)**, such as **Tarjan’s** and **Kosaraju’s**, are for **directed graphs**.  

4. **Disconnected Graphs:**
   - **Kruskal’s Algorithm** may not form an MST if the graph is **disconnected**.  
   - **PageRank** struggles with small or disconnected graphs due to lack of meaningful link structures.  

5. **Flow Algorithms:**
   - **Ford-Fulkerson** and **Edmonds-Karp** have issues with **irrational capacities**, leading to convergence problems.  

---

### 💡 **Quick Summary:**

- ✅ **Acyclic Graph Algorithms:** Topological Sort, Kahn’s Algorithm  
- 🔁 **Cyclic Graph Algorithms:** Hierholzer’s (Eulerian paths), SCC Algorithms (Tarjan, Kosaraju)  
- ⚠️ **Fails with Negative Cycles:** Bellman-Ford, Johnson’s, Floyd-Warshall  
- 🌐 **For Both Directed & Undirected:** BFS, DFS, Dijkstra, Floyd-Warshall  

Let me know if you'd like me to elaborate on any algorithm or concept! 🚀