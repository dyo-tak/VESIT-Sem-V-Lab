import queue
import heapq

start_state = [
    [1, 8, 4],
    [5, 0, 3],
    [6, 2, 7]
]

goal_state = [
    [8, 3, 4],
    [1, 0, 5],
    [7, 2, 6]
]

goal_positions = {}
for i in range(3):
    for j in range(3):
        goal_positions[goal_state[i][j]] = (i, j)

def heuristic(state):
    total_distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                goal_row, goal_col = goal_positions[state[i][j]]
                total_distance += abs(i - goal_row) + abs(j - goal_col)
    return total_distance

def solve(start_state, goal_state):
    open_set = []
    heapq.heappush(open_set, (heuristic(start_state), start_state))
    came_from = {tuple(map(tuple, start_state)): None}
    g_score = {tuple(map(tuple, start_state)): 0}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal_state:
            path = []
            while current:
                path.append(current)
                current = came_from.get(tuple(map(tuple, current)), None)
            path.reverse()
            return path

        for move in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_state = [list(row) for row in current]
            zero_row, zero_col = [(i, row.index(0)) for i, row in enumerate(current) if 0 in row][0]
            new_row, new_col = zero_row + move[0], zero_col + move[1]

            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_state[zero_row][zero_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[zero_row][zero_col]
                new_state_tuple = tuple(map(tuple, new_state))
                tentative_g_score = g_score[tuple(map(tuple, current))] + 1

                if new_state_tuple not in g_score or tentative_g_score < g_score[new_state_tuple]:
                    g_score[new_state_tuple] = tentative_g_score
                    f_score = tentative_g_score + heuristic(new_state)
                    heapq.heappush(open_set, (f_score, new_state))
                    came_from[new_state_tuple] = current

    return None

solution_path = solve(start_state, goal_state)

if solution_path:
    for step, state in enumerate(solution_path):
        print(f"Step {step}:\n")
        for row in state:
            print(row)
        print("\n")
else:
    print("No solution found.")

