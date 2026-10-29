from itertools import permutations

# Function to solve TSP
def travelling_salesman(graph, start):
    cities = list(range(len(graph)))
    cities.remove(start)
    min_cost = float('inf')
    best_path = None

    # Generate all possible tours
    for perm in permutations(cities):
        current_cost = 0
        current_path = [start]
        k = start

        for city in perm:
            current_cost += graph[k][city]
            current_path.append(city)
            k = city

        current_cost += graph[k][start]
        current_path.append(start)

        if current_cost < min_cost:
            min_cost = current_cost
            best_path = current_path

    return best_path, min_cost


# Main Program
n = int(input("Enter the number of cities: "))

print("Enter the cost matrix:")
graph = []

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

start = int(input("Enter the starting city (0 to {}): ".format(n - 1)))

path, cost = travelling_salesman(graph, start)

print("\nOptimal Path:", " -> ".join(map(str, path)))
print("Minimum Cost:", cost)
# OUTPUT
# Enter the number of cities: 3
# Enter the cost matrix row by row:
# 0 45 56
# 45 0 78
# 56 78 0
# Enter the starting city (0 to 2): 2
# Optimal Path: 2 -> 0 -> 1 -> 2
# Minimum Cost: 179   
