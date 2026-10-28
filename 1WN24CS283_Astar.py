
import heapq

def heuristic(state, goal):
    distance = 0
    for i, tile in enumerate(state):
        if tile != 0:
            j = goal.index(tile)
            distance += abs(i // 3 - j // 3)
            distance += abs(i % 3 - j % 3)
    return distance

def neighbors(state):
    result = []
    zero = state.index(0)
    row, col = zero // 3, zero % 3

    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        r, c = row + dr, col + dc

        if 0 <= r < 3 and 0 <= c < 3:
            pos = r * 3 + c
            new_state = list(state)
            new_state[zero], new_state[pos] = (
                new_state[pos], new_state[zero]
            )
            result.append(tuple(new_state))

    return result

def astar(start, goal):
    pq = [(heuristic(start, goal), 0, start)]
    cost = {start: 0}
    parent = {start: None}

    while pq:
        f, g, current = heapq.heappop(pq)

        if g != cost[current]:
            continue

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]

        for nxt in neighbors(current):
            new_cost = g + 1

            if nxt not in cost or new_cost < cost[nxt]:
                cost[nxt] = new_cost
                parent[nxt] = current
                heapq.heappush(
                    pq, (new_cost + heuristic(nxt, goal),
                         new_cost, nxt)
                )

    return None

def read_state(message):
    while True:
        values = tuple(map(int, input(message).split()))
        if len(values) == 9 and set(values) == set(range(9)):
            return values
        print("Enter 9 numbers from 0 to 8 without repetition.")

start = read_state("Enter initial state (0 represents blank): ")
goal = read_state("Enter goal state (0 represents blank): ")

path = astar(start, goal)

if path:
    print("\nSolution found in", len(path) - 1, "moves:")
    for state in path:
        for i in range(0, 9, 3):
            print(*state[i:i+3])
        print()
else:
    print("No solution exists.")
