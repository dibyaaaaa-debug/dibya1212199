from collections import deque

def dfs(graph, start_node):
    visited = []
    stack = [start_node]

    while stack:
        current_node = stack.pop()

        if current_node not in visited:
            print(f"Exploring node:{current_node}:")
            visited.append(current_node)

            # Add neighbors to stack in reverse order to preserve a clean left-to-right discovery 
            for neighbour in reversed(graph.get(current_node, [])):
                if neighbour not in visited:
                    stack.append(neighbour)

print("---Build Your Graph")
student_graph = {}

num_edges = int(input("How many edges does your graph have? "))

print("Enter each edge separated by a space (e.g., A B):")

for i in range(num_edges):
    u, v = input(f"Edge {i + 1}: ").split()

    if u not in student_graph:
        student_graph[u] = []
    if v not in student_graph:
        student_graph[v] = []

    student_graph[u].append(v)
    student_graph[v].append(u)

start = input("Enter the starting node for DFS: ")

print(f"\nYour Graph Dictionary: {student_graph}")
print("Starting DFS Traversal...")

dfs(student_graph, start)
# OUTPUT
# ---Build Your Graph
# How many edges does your graph have? 3
# Enter each edge separated by a space (e.g., A B):
# Edge 1: A B
# Edge 2: B C
# Edge 3: C D
# Enter the starting node for DFS: A

# Your Graph Dictionary: {'A': ['B'], 'B': ['A', 'C'], 'C': ['B', 'D'], 'D': ['C']}
# Starting DFS Traversal...
# Exploring node:A:
# Exploring node:B:
# Exploring node:C:
# Exploring node:D:
