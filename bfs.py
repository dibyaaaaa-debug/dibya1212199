from collections import deque

def bfs(graph, start_node):
    visited = []
    queue = deque([start_node])
    
    while queue:
        current_node = queue.popleft()
        if current_node not in visited:
            print(f"Exploring node:{current_node}:")
            visited.append(current_node)
            for neighbour in graph.get(current_node, []):
                if neighbour not in visited:
                    queue.append(neighbour)

print("---Build Your Graph")
student_graph = {}
num_edges = int(input("How many edges does your graph have? "))

print("Enter each edge separated by a space(e.g., A B):")
for i in range(num_edges):
    u, v = input(f"Edge {i + 1}: ").split()
    if u not in student_graph:
        student_graph[u] = []
    if v not in student_graph:
        student_graph[v] = []
    student_graph[u].append(v)
    student_graph[v].append(u)

start = input("Enter the starting node for BFS: ")
print(f"\nYour Graph Dictionary: {student_graph}")
print("Starting BFS Traversal...")
bfs(student_graph, start)
from collections import deque

def bfs(graph, start_node):
    visited = []
    queue = deque([start_node])
    
    while queue:
        current_node = queue.popleft()
        if current_node not in visited:
            print(f"Exploring node:{current_node}:")
            visited.append(current_node)
            for neighbour in graph.get(current_node, []):
                if neighbour not in visited:
                    queue.append(neighbour)

print("---Build Your Graph")
student_graph = {}
num_edges = int(input("How many edges does your graph have? "))

print("Enter each edge separated by a space(e.g., A B):")
for i in range(num_edges):
    u, v = input(f"Edge {i + 1}: ").split()
    if u not in student_graph:
        student_graph[u] = []
    if v not in student_graph:
        student_graph[v] = []
    student_graph[u].append(v)
    student_graph[v].append(u)

start = input("Enter the starting node for BFS: ")
print(f"\nYour Graph Dictionary: {student_graph}")
print("Starting BFS Traversal...")
bfs(student_graph, start)
# OUTPUT
# ---Build Your Graph
# How many edges does your graph have? 3
# Enter each edge separated by a space(e.g., A B):
# Edge 1: A B
# Edge 2: B C
# Edge 3: C D
# Enter the starting node for BFS: A

# Your Graph Dictionary: {'A': ['B'], 'B': ['A', 'C'], 'C': ['B', 'D'], 'D': ['C']}
# Starting BFS Traversal...
# Exploring node:A:
# Exploring node:B:
# Exploring node:C:
# Exploring node:D:

