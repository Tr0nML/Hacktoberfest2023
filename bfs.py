from collections import defaultdict, deque

# Function to create an adjacency list representation of a graph
def create_graph():
    graph = defaultdict(list)
    num_nodes = int(input("Enter the number of nodes: "))
    num_edges = int(input("Enter the number of edges: "))
    
    print("Enter edges in the format 'node1 node2', e.g., 'A B'")
    for i in range(num_edges):
        while True:
            edge = input(f"Enter edge {i + 1}: ").split()
            if len(edge) == 2:
                u, v = edge
                graph[u].append(v)
                break
            else:
                print("Invalid input format")
    return graph

# Function for Breadth-First Search (BFS)
def bfs_search(graph, start, target):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node == target:
            return True  # Target node found
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return False  # Target node not found

# Create the graph based on user input
user_graph = create_graph()
print(user_graph)
while True:
    start_node = input("Enter the starting node for BFS search: ").strip()
    if start_node in user_graph:
        break
    else:
        print("Invalid starting node")

target_node = input("Enter the target node for BFS search: ").strip()

# Perform BFS search
if bfs_search(user_graph, start_node, target_node):
    print(f"The target node '{target_node}' is reachable from '{start_node}' using BFS.")
else:
    print(f"The target node '{target_node}' is not reachable from '{start_node}' using BFS.")

