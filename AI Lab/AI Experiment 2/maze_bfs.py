import queue
from typing import NamedTuple

class Coordinate(NamedTuple):
    x: int
    y: int

class Maze:

    def __init__(self):    
        self.start = ""
        self.goal = "="
        self.path = ""
        self.block = "󰚍"

    def create_maze(self) -> list:
        maze = []
        
        maze.append(["󰚍", "󰚍", "󰚍", "󰚍", "󰚍", self.start, "󰚍", "󰚍", "󰚍", "󰚍", "󰚍"])
        maze.append(["󰚍", " ", " ", " ", "󰚍", " ", " ", " ", " ", " ", "󰚍"])
        maze.append(["󰚍", "󰚍", "󰚍", " ", "󰚍", "󰚍", "󰚍", "󰚍", "󰚍", " ", "󰚍"])
        maze.append(["󰚍", " ", " ", " ", "󰚍", " ", " ", " ", " ", " ", "󰚍"])
        maze.append(["󰚍", " ", "󰚍", "󰚍", "󰚍", " ", "󰚍", "󰚍", "󰚍", "󰚍", "󰚍"])
        maze.append(["󰚍", " ", " ", " ", " ", " ", " ", " ", " ", " ", "󰚍"])
        maze.append(["󰚍", " ", "󰚍", "󰚍", "󰚍", " ", "󰚍", "󰚍", "󰚍", " ", "󰚍"])
        maze.append(["󰚍", " ", "󰚍", " ", " ", " ", "󰚍", " ", " ", " ", "󰚍"])
        maze.append(["󰚍", " ", "󰚍", "󰚍", "󰚍", "󰚍", "󰚍", " ", "󰚍", "󰚍", "󰚍"])
        maze.append(["󰚍", " ", " ", " ", " ", " ", "󰚍", " ", " ", " ", "󰚍"])
        maze.append(["󰚍", "󰚍", "󰚍", "󰚍", "󰚍", self.goal, "󰚍", "󰚍", "󰚍", "󰚍", "󰚍"])

        return maze

    def is_allowed(self, maze, moves=""):
        start_index = maze[0].index(self.start)
        x = start_index
        y = 0

        for i in moves:
            if i == "L":
                x -= 1
            if i == "R":
                x += 1
            if i == "U":
                y -= 1
            if i == "D":
                y += 1

        if x <= 0 or y <= 0:
            return False
        
        if maze[x][y] == "󰚍":
            return False
        
        return True

                

    def print_maze(self, maze):
        for row in maze:
            print(" ".join(row))

        


m = Maze()
maze = m.create_maze()
m.is_allowed(maze)
m.print_maze(maze)