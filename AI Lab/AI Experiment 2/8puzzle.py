import random

def generate_maze(width, height):
    maze = []

    for _ in range(height):
        row = []
        for _ in range(width):
            row.append("#")
        maze.append(row)

    start_x, start_y = random.randint(1, width - 2), 0
    goal_x, goal_y = random.randint(1, width - 2), height - 1

    maze[start_y][start_x] = "S"
    maze[goal_y][goal_x] = "G"

    stack = [(start_x, start_y)]

    while stack:
        x, y = stack[-1]
        maze[y][x] = " "

        neighbors = [(x + dx, y + dy) for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]]
        unvisited_neighbors = [(nx, ny) for nx, ny in neighbors if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == "#"]

        if unvisited_neighbors:
            nx, ny = random.choice(unvisited_neighbors)
            stack.append((nx, ny))
            maze[(ny + y) // 2][(nx + x) // 2] = " "
        else:
            stack.pop()

    return maze

def print_maze(maze):
    for row in maze:
        print("".join(row))

if __name__ == "__main__":
    width, height = 11, 11
    maze = generate_maze(width, height)
    print_maze(maze)

