import heapq

# Function to calculate Manhattan Distance heuristic
def heuristic(state, goal):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                x, y = divmod(goal.index(state[i][j]), 3)
                distance += abs(x - i) + abs(y - j)
    return distance

# Function to flatten 2D list to 1D
def flatten(state):
    return [num for row in state for num in row]

# Function to find neighbors (possible moves)
def get_neighbors(state):
    neighbors = []
    x, y = next((i, j) for i in range(3) for j in range(3) if state[i][j] == 0)
    moves = [(-1,0), (1,0), (0,-1), (0,1)]  # up, down, left, right

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [list(row) for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

# A* Algorithm
def a_star(start, goal):
    goal_flat = flatten(goal)
    pq = []
    heapq.heappush(pq, (0, start, []))
    visited = set()

    while pq:
        f, state, path = heapq.heappop(pq)
        state_tuple = tuple(flatten(state))

        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        if flatten(state) == goal_flat:
            return path + [state]

        for neighbor in get_neighbors(state):
            g = len(path) + 1
            h = heuristic(neighbor, goal_flat)
            f_new = g + h
            heapq.heappush(pq, (f_new, neighbor, path + [state]))
    return None

# Initial and goal states
start_state = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Run A*
result = a_star(start_state, goal_state)

if result:
    print("Path to Goal:")
    for step in result:
        for row in step:
            print(row)
        print()
else:
    print("No solution found.")
