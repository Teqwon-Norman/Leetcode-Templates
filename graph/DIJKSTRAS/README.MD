# INTRODUCTION TO DIJKSTRA'S ALGORITHM

### PURPOSE AND USE CASES
-------------------------
- You can find the shortest path between nodes in a graph

- You can find the shortest path from a node to all other nodes in a graph

- The dijkstra's algorithm is used in GPS devices to find the shortest path between the current location and the destination

- Various projects are created using this algorithm, such as solving a complex maze puzzle very quickly and visualize the shortest path being drawn. Starting from a starting point and reaching the target it will highlight the shortest path when it is finished

### SOLUTION
------------
- Dijkstra's algorithm basically starts from a certain node or source node, and it analyzes the graph to find the shortest path between that node and all the other nodes in the graph

- It keeps track of the currently known shortest distance from each node to the source node and it updates these values if it finds a shorter path

- Once the shortest path has been found between the source node and another node, that newly visited node will be marked as "visited" and added towards the current shortest path we are finding

- We continue this process until all nodes in the graph have been added to the path. Then we will have a path that connects the source node to all other nodes following the shortest path possible to reach each node

### REQUIREMENTS
----------------
- Dijkstra's algorithm is designed for graphs with non-negative weights on their edges. The algorithm aims to find the shortest path between a source node and all other nodes in the graph, based on the assumption that shorter paths have smaller weights

- Dijkstra's algorithm does not take into account additional factors like traffic congestion, road closures, or other real-world variables. This is a limitation of Dijkstra's algorithm in modeling real-world situations accurately

- More advanced algorithms such as A* (A star) or variants of Dijkstra's algorithm with additional features can be used. These algorithms incorporate heuristics or extra information to make more informed decisions about which paths to explore, taking into account both the graph weights and external conditions