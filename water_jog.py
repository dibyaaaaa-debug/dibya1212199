from collections import deque

#function to solve water jog problem using bfs
def water_jog(capacity_1,capacity_2,target):
    visited=set()
    queue=deque()
    queue.append((0,0,[]))  # (amount_1, amount_2, path_list)
    while queue:
        jog1,jog2,path=queue.popleft()
        if (jog1,jog2) in visited:
            continue
        visited.add((jog1,jog2))
        path=path+[(jog1,jog2)]
        if jog1 == target or jog2 == target or jog1 + jog2 == target:
            return path
        # Generate all possible next states
        next_states = [
            (capacity_1, jog2, path),  # Fill jug 1
            (jog1, capacity_2, path),  # Fill jug 2
            (0, jog2, path),  # Empty jug 1
            (jog1, 0, path),  # Empty jug 2
            (min(capacity_1, jog1 + jog2), max(0, jog2 - (capacity_1 - jog1)), path),  # Pour jug 2 into jug 1
            (max(0, jog1 - (capacity_2 - jog2)), min(capacity_2, jog1 + jog2), path)   # Pour jug 1 into jug 2
        ]
        for state in next_states:
            if (state[0], state[1]) not in visited:
                queue.append(state)
    return None

jog1=int(input("enter capacity of jog1:"))
jog2=int(input("enter capacity of jog2:"))
target=int(input("enter target amount:"))
solution=water_jog(jog1,jog2,target)
if solution:
    print("\nsteps to reach the target")
    for step in solution:
        print(step)
else:
    print("no solution exists")
