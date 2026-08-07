import heapq

def prim(graph, start):
    visited = set()
    min_heap = [(0, start)]
    mst = []
    total_cost = 0

    while min_heap:
        weight, node = heapq.heappop(min_heap)

        if node in visited:
            continue

        visited.add(node)
        total_cost += weight

        if weight != 0:
            mst.append((node, weight))

        for neighbor, edge_weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(
                    min_heap,
                    (edge_weight, neighbor)
                )

    return mst, total_cost


graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('C', 1), ('D', 5)],
    'C': [('A', 2), ('B', 1), ('D', 8)],
    'D': [('B', 5), ('C', 8)]
}

mst, cost = prim(graph, 'A')

print("Minimum Spanning Tree:")
print(mst)
print("Total cost:", cost)