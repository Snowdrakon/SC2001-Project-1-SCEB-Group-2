import sys
import heapq

# Adjacency Matrix and Array
def dijkstra(adj_matrix, source):
    num_vertices = len(adj_matrix)
    d = [float('inf')] * num_vertices
    d[source] = 0
    priority_queue = list(range(num_vertices))

    while priority_queue:
        # Find vertex with minimum distance in the priority queue
        min_distance_vertex = min(priority_queue, key=lambda v: d[v])
        priority_queue.remove(min_distance_vertex)

        # Update distances for neighbors
        for neighbor in range(num_vertices):
            if adj_matrix[min_distance_vertex][neighbor] != 0:
                new_distance = d[min_distance_vertex] + adj_matrix[min_distance_vertex][neighbor]
                if new_distance < d[neighbor]:
                    d[neighbor] = new_distance

    return d

# Test
if __name__ == "__main__":
    adjacency_matrix = [
        [0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
    ]

    source_vertex = 0
    shortest_distances = dijkstra(adjacency_matrix, source_vertex)
    print("Shortest distances from source vertex:")
    for i, distance in enumerate(shortest_distances):
        print(f"Vertex {i}: {distance}")


# Adjacency List and Heap
def dijkstra2(adj_list, source):
    num_vertices = len(adj_list)
    distances = [float('inf')] * num_vertices
    distances[source] = 0
    priority_queue = [(0, source)]  # (distance, vertex)

    while priority_queue:
        # Pop vertex with smallest distance from the min-heap
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # If already processed vertex w smaller distance, skip
        if current_distance > distances[current_vertex]:
            continue

        # Update distances for neighbors
        for neighbor, edge_weight in adj_list[current_vertex]:
            new_distance = distances[current_vertex] + edge_weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                # Push the updated distance and neighbor into the min-heap
                heapq.heappush(priority_queue, (new_distance, neighbor))

    return distances

# Test
if __name__ == "__main__":
    adjacency_list = [
        [(1, 4), (7, 8)],
        [(0, 4), (2, 8), (7, 11)],
        [(1, 8), (3, 7), (5, 4), (8, 2)],
        [(2, 7), (4, 9), (5, 14)],
        [(3, 9), (5, 10)],
        [(2, 4), (3, 14), (4, 10), (6, 2)],
        [(5, 2), (7, 1), (8, 6)],
        [(0, 8), (1, 11), (6, 1), (8, 7)],
        [(2, 2), (6, 6), (7, 7)]
    ]

    source_vertex = 0
    shortest_distances = dijkstra2(adjacency_list, source_vertex)
    print("Shortest distances from source vertex:")
    for i, distance in enumerate(shortest_distances):
        print(f"Vertex {i}: {distance}")
