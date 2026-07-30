def dfs (graph,start_node):
  visited=[]
  stack=[start_node]
  while stack:
    current_node=stack.pop()
    if current_node not in visited:
      print(f"exploring node:{current_node}")
      visited.append(current_node)
      for neighor in graph.get(current_node,[]):
        if neighor not in visited:
          stack.append(neighor)
    return visited

  

graph = {}

n = int(input("Enter the number of nodes: "))

for i in range(n):
    node = input("Enter node: ")
    neighbors = input(f"Enter neighbors of {node} (space-separated): ").split()
    graph[node] = neighbors6
start_node = input("Enter the starting node: ")
traversal = dfs(graph, start_node)
print("DFS Traversal:", traversal)
