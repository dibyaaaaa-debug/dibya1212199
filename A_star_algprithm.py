#DT:27.08.26
# WAP TO IMPLEMENT A* ALGORITM.

def a_star(graph, heuristic, start, goal):
    open_list = [start]
    closed_list = []

    # g_cost = cost from start node
    g_cost = {start: 0}

    # Parent dictionary to reconstruct the path
    parent = {start: None}

    while open_list:
        # Select node having minimum f(n) = g(n) + h(n)
        current = open_list[0]

        for node in open_list:
            f_current = g_cost[current] + heuristic[current]
            f_node = g_cost[node] + heuristic[node]

            if f_node < f_current:
                current = node

        # Goal reached
        if current == goal:
            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()

            print("\nShortest Path:", " -> ".join(path))
            print("Total Cost:", g_cost[goal])
            return

        open_list.remove(current)
        closed_list.append(current)

        # Check all neighboring nodes
        for neighbor, cost in graph[current]:

            if neighbor in closed_list:
                continue

            new_cost = g_cost[current] + cost

            # If neighbor is new or a better path is found
            if neighbor not in open_list or new_cost < g_cost.get(neighbor, float('inf')):

                g_cost[neighbor] = new_cost
                parent[neighbor] = current

                if neighbor not in open_list:
                    open_list.append(neighbor)

    print("\nNo path found.")


# ---------------- USER INPUT ----------------

graph = {}

n = int(input("Enter number of nodes: "))

print("\nEnter node names:")
nodes = []

for i in range(n):
    node = input(f"Node {i + 1}: ")
    nodes.append(node)
    graph[node] = []

# Enter edges
e = int(input("\nEnter number of edges: "))

print("\nEnter edges in the following format:")
print("Source Destination Cost")

for i in range(e):
    source = input(f"\nEdge {i + 1} source: ")
    destination = input(f"Edge {i + 1} destination: ")
    cost = int(input("Cost: "))

    graph[source].append((destination, cost))

# Enter heuristic values
heuristic = {}

print("\nEnter heuristic values h(n):")

for node in nodes:
    heuristic[node] = int(input(f"h({node}): "))

# Start and goal
start = input("\nEnter start node: ")
goal = input("Enter goal node: ")

# Run A* Algorithm
a_star(graph, heuristic, start, goal)
#OUTPUT
# Enter number of nodes: 4

# Enter node names:
# Node 1: A
# Node 2: B
# Node 3: C
# Node 4: D

# Enter number of edges: 4

# Enter edges in the following format:
# Source Destination Cost

# Edge 1 source: A
# Edge 1 destination: B
# Cost: 1

# Edge 2 source: A
# Edge 2 destination: C
# Cost: 5

# Edge 3 source: B
# Edge 3 destination: D
# Cost: 3

# Edge 4 source: C
# Edge 4 destination: D
# Cost: 1

# Enter heuristic values h(n):
# h(A): 4
# h(B): 2
# h(C): 1
# h(D): 0

# Enter start node: A
# Enter goal node: D

# Shortest Path: A -> B -> D
# Total Cost: 4


