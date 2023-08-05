import queue
class Maze:

    def __init__(self):    
        self.start = "S"
        self.goal = "G"
        self.path = "."
        self.block = "#"
        self.START = "S"
        self.GOAL = "G"
        self.PATH = "."
        self.BLOCK = "#"

    def create_maze(self) -> list:
        maze = []
        
        maze.append([self.BLOCK, self.BLOCK, self.BLOCK, self.BLOCK, self.BLOCK, self.START, self.BLOCK, self.BLOCK, self.BLOCK, self.BLOCK, self.BLOCK])
        maze.append([self.BLOCK, " ", " ", " ", self.BLOCK, " ", " ", " ", " ", " ", self.BLOCK])
        maze.append([self.BLOCK, self.BLOCK, self.BLOCK, " ", self.BLOCK, self.BLOCK, self.BLOCK, self.BLOCK, self.BLOCK, " ", self.BLOCK])
        maze.append([self.BLOCK, " ", " ", " ", self.BLOCK, " ", " ", " ", " ", " ", self.BLOCK])
        maze.append([self.BLOCK, " ", self.BLOCK, self.BLOCK, self.BLOCK, " ", self.BLOCK, self.BLOCK, self.BLOCK, self.BLOCK, self.BLOCK])
        maze.append([self.BLOCK, " ", " ", " ", " ", " ", " ", " ", " ", " ", self.BLOCK])
        maze.append([self.BLOCK, " ", self.BLOCK, self.BLOCK, self.BLOCK, " ", self.BLOCK, self.BLOCK, self.BLOCK, " ", self.BLOCK])
        maze.append([self.BLOCK, " ", self.BLOCK, " ", " ", " ", self.BLOCK, " ", " ", " ", self.BLOCK])
        maze.append([self.BLOCK, " ", self.BLOCK, self.BLOCK, self.BLOCK, self.BLOCK, self.BLOCK, " ", self.BLOCK, self.BLOCK, self.BLOCK])
        maze.append([self.BLOCK, " ", " ", " ", " ", " ", self.BLOCK, " ", " ", " ", self.BLOCK])
        maze.append([self.BLOCK, self.BLOCK, self.BLOCK, self.BLOCK, self.BLOCK, self.GOAL, self.BLOCK, self.BLOCK, self.BLOCK, self.BLOCK, self.BLOCK])

        return maze

    def is_allowed(self, maze, moves=""):
        start_index = maze[0].index(self.start)
        x = start_index
        y = 0

        for i in moves:
            if i == "L": x -= 1
            if i == "R": x += 1
            if i == "U": y -= 1
            if i == "D": y += 1

        if x <= 0 or y <= 0:
            return False
        
        if x >= len(maze) or y >= len(maze[0]):
            return False

        if maze[y][x] == self.block:
            return False

        return True
    
    def is_solved(self, maze, moves=""):
        start_index = maze[0].index(self.start)
        x = start_index
        y = 0

        print(moves)

        for i in moves:
            if i == "L": x -= 1
            if i == "R": x += 1
            if i == "U": y -= 1
            if i == "D": y += 1

        if x <= 0 or y <= 0:
            return False
        
        if x > len(maze) or y > len(maze[0]):
            return False

        if maze[y][x] == self.block:
            return False
        
        if maze[y][x] == self.goal:
            print(moves)
            return True
                

    def print_maze(self, maze, moves=''):
        print()
        my_maze = maze
        start_index = maze[0].index(self.start)
        x = start_index
        y = 0

        for i in moves:
            if i == "L": x -= 1
            if i == "R": x += 1
            if i == "U": y -= 1
            if i == "D": y += 1
            my_maze[y][x] = self.path

        for row in maze:
            print(" ".join(row))
        print()

        


m = Maze()
maze = m.create_maze()

my_queue = queue.Queue()
my_queue.put("")
path = ""

possible_moves = ['L', 'R', 'U', 'D']

m.print_maze(maze)

while not m.is_solved(maze=maze, moves=path):
    path = my_queue.get()
    
    for i in possible_moves:
        if (i == 'L' and path.endswith('R')):
            continue
        if (i == 'R' and path.endswith('L')):
            continue
        if (i == 'D' and path.endswith('U')):
            continue
        if (i == 'U' and path.endswith('D')):
            continue

        temp = path + i
        
        if m.is_allowed(maze, temp):
            my_queue.put(temp)

m.print_maze(maze, path)