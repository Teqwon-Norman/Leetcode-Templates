import heapq

def dijkstras(n: int, graph: List[List[int]]) -> int:
    adj = [ [] for _ in range(n) ]
    # u and v represents the nodes in the graph
    # w represents the weight to travel from u -> v or v -> u
    for u, v, w in graph:
        adj[u].append((v, w))
        adj[v].append((u, w))
    

    heap = []
    distance = [ float('inf') ] * n
    paths = [0] * n

    distance[0], paths[0] = 0, 1
    heapq.heapify(heap)
    heapq.heappush(heap, (0, 0))

    while heap:
        dist, node = heapq.heappop(heap)
        for adjNode, weight in adj[node]:
            if dist + weight < distance[adjNode]:
                distance[adjNode] = dist + weight
                heapq.heappush(heap, (dist + weight, adjNode))
                paths[adjNode] = paths[node]

            elif dist + weight == distance[adjNode]:
                paths[adjNode] += paths[node]
    return paths[n - 1]